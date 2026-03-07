"""An agent graph with a post-response vibe check loop.

After the agent responds, a secondary node evaluates whether the response
matches the desired vibe (friendly, concise, on-topic). If not, loop back
to the agent; if yes or after a message limit, end.
"""
from __future__ import annotations

from pydantic import BaseModel, Field

from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import AIMessage

from app.state import MessagesState
from app.models import get_chat_model
from app.tools import get_tool_belt


# Desired vibe: friendly, concise, and on-topic
DESIRED_VIBE = "friendly, concise, and directly on-topic (no unnecessary tangents)"


class VibeResult(BaseModel):
    matches_vibe: bool = Field(
        description="True if the response matches the desired vibe (friendly, concise, on-topic); False if it's too formal, verbose, or off-topic."
    )


def _build_model_with_tools():
    """Return a chat model instance bound to the current tool belt."""
    model = get_chat_model()
    return model.bind_tools(get_tool_belt())


def call_model(state: MessagesState) -> dict:
    """Invoke the model with the accumulated messages and append its response."""
    model = _build_model_with_tools()
    messages = state["messages"]
    response = model.invoke(messages)
    return {"messages": [response]}


def route_to_action_or_vibe(state: MessagesState):
    """Decide whether to execute tools or run the vibe checker."""
    last_message = state["messages"][-1]
    if getattr(last_message, "tool_calls", None):
        return "action"
    return "vibe"


_vibe_prompt = ChatPromptTemplate.from_template(
    "You are a vibe checker. Given a user query and the assistant's response, decide if the response "
    "matches the desired vibe: {desired_vibe}\n\n"
    "User query:\n{initial_query}\n\n"
    "Assistant response:\n{final_response}\n\n"
    "Does this response match the vibe? Consider: Is it friendly (not cold or robotic)? "
    "Concise (not overly long or repetitive)? On-topic (addresses the query without unnecessary tangents)?"
)


def vibe_node(state: MessagesState) -> dict:
    """Evaluate whether the latest response matches the desired vibe."""
    if len(state["messages"]) > 10:
        return {"messages": [AIMessage(content="VIBE:END")]}

    initial_query = state["messages"][0]
    final_response = state["messages"][-1]

    structured_model = get_chat_model(model_name="gpt-4.1-mini").with_structured_output(VibeResult)
    result = (_vibe_prompt.partial(desired_vibe=DESIRED_VIBE) | structured_model).invoke(
        {
            "initial_query": initial_query.content,
            "final_response": final_response.content,
        }
    )

    decision = "Y" if result.matches_vibe else "N"
    return {"messages": [AIMessage(content=f"VIBE:{decision}")]}


def vibe_decision(state: MessagesState):
    """Terminate on 'VIBE:Y' or end guard; otherwise loop back to agent."""
    if any(getattr(m, "content", "") == "VIBE:END" for m in state["messages"][-1:]):
        return END

    last = state["messages"][-1]
    text = getattr(last, "content", "")
    if "VIBE:Y" in text:
        return "end"
    return "continue"


def build_graph():
    """Build an agent graph with a vibe-check evaluation loop."""
    graph = StateGraph(MessagesState)
    tool_node = ToolNode(get_tool_belt())
    graph.add_node("agent", call_model)
    graph.add_node("action", tool_node)
    graph.add_node("vibe", vibe_node)
    graph.add_edge(START, "agent")
    graph.add_conditional_edges(
        "agent",
        route_to_action_or_vibe,
        {"action": "action", "vibe": "vibe"},
    )
    graph.add_conditional_edges(
        "vibe",
        vibe_decision,
        {"continue": "agent", "end": END, END: END},
    )
    graph.add_edge("action", "agent")
    return graph


graph = build_graph().compile()
