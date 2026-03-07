## # Session 15: Build & Serve Agentic Graphs with LangGraph


| 📰 Session Sheet                                                                                          | ⏺️ Recording                                                                                                                                          | 🖼️ Slides                                                                                                                                                                         | 👨‍💻 Repo    | 📝 Homework                                                                 | 📁 Feedback                                         |
| --------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- | --------------------------------------------------------------------------- | --------------------------------------------------- |
| [Agent Servers](https://github.com/AI-Maker-Space/AIE9/tree/main/00_Docs/Session_Sheets/15_Agent_Servers) | [Recording!](https://us02web.zoom.us/rec/share/lORjByDju6fv4TdE3r93dorY3aNgmSKL_Qk_cX_AMcCQ6cNfSW77unaA1LMVV60.OcI8uEnfVmRAgjSn) passcode: `Dc@&pv1T` | [Session 15 Slides](https://www.canva.com/design/DAG-EJqkRaM/FR3WG_yMA5_BqbWpQlHR9g/edit?utm_content=DAG-EJqkRaM&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton) | You are here! | [Session 15 Assignment: Agent Servers](https://forms.gle/Vb3HNDsyVPQ1jqKX7) | [Feedback 3/3](https://forms.gle/kYmhbVUEMog16mKv8) |


### Prerequisites

Before starting, ensure you have the following:

- **Python 3.11+** installed
- An **OpenAI API Key**
- A **Tavily API Key**
- (Optional) **LangSmith** credentials for tracing

Create a `.env` file in this directory with your API keys:

1. Run `uv sync` to install dependencies.

# Build 🏗️

Run the repository and complete the following:

- 🤝 Breakout Room Part #1 — Building and serving your LangGraph Agent Graph
  - Task 1: Getting Dependencies & Environment
    - Configure `.env` (OpenAI, Tavily, optional LangSmith)
  - Task 2: Serve the Graph Locally
    - `uv run langgraph dev` (API on [http://localhost:2024](http://localhost:2024))
  - Task 3: Call the API from a different terminal
    - `uv run test_served_graph.py` (sync SDK example)
  - Task 4: Explore assistants (from `langgraph.json`)
    - `agent` → `simple_agent` (tool-using agent)
    - `agent_helpful` → `agent_with_helpfulness` (separate helpfulness node)
- 🤝 Breakout Room Part #2 — Using LangSmith Studio to visualize the graph
  - Task 1: Open Studio while the server is running
    - [https://smith.langchain.com/studio?baseUrl=http://localhost:2024](https://smith.langchain.com/studio?baseUrl=http://localhost:2024)
  - Task 2: Visualize & Stream
    - Start a run and observe node-by-node updates
  - Task 3: Compare Flows
    - Contrast `agent` vs `agent_helpful` (tool calls vs helpfulness decision)

🚧 Advanced Build 🚧 (OPTIONAL - *open this section for the requirements*)

> NOTE: This can be done in place of the Main Assignment

- Create and deploy a locally hosted MCP server with FastMCP.
- Extend your tools in `tools.py` to allow your LangGraph to consume the MCP Server.

When submitting, provide:

- Your Loom video link demonstrating the MCP server integration
- The GitHub URL to your completed Advanced Build

Have fun!

### Questions & Activities

#### Question 1:

What is the key architectural difference between the `simple_agent` and `agent_with_helpfulness` graphs? Specifically, explain how the helpfulness evaluation loop works and what mechanisms are in place to prevent it from running indefinitely.

##### Answer:

The main difference is that **agent_with_helpfulness** has an additional evaluation loop after the LLM generates a response. A helpfulness node evaluates whether that response is helpful for the original question (using the first message as the query and the latest response). It adds a message to state with the decision: `HELPFULNESS:Y` or `HELPFULNESS:N`. If **N**, the graph loops back to the agent to generate again; if **Y**, it goes to the end state. To prevent infinite looping, the helpfulness node checks if the number of messages in state is greater than 10—if so, it injects `HELPFULNESS:END` and the graph routes to the end state even if the response was not deemed helpful.

#### Question 2:

What is the role of `langgraph.json` in the LangGraph Deployments? Describe each of its key fields and how the platform uses this file to discover and serve your graphs.

##### Answer:

`langgraph.json` is the **configuration file** that the LangGraph CLI (and LangGraph Deployments / Agent Server) use to **discover your graphs, resolve dependencies, and serve the API**. The CLI looks for this file in the project directory when you run `langgraph dev`, `langgraph build`, or `langgraph up`.

**Key fields and how the platform uses them:**

- **`version`** — Schema version of the config file so the platform can parse it correctly.

- **`dependencies`** — Tells the platform **where to find package dependencies**. A value of `["."]` means “use the current directory” (e.g. a local `pyproject.toml` or `requirements.txt`). The server installs these before loading your graphs so your graph code can import its dependencies.

- **`env`** — Path to the **environment file** (e.g. `".env"`). The platform loads these variables into the process so the server and your graphs can access API keys and other config at runtime.

- **`python_version`** — **Python version** used to build/run the server (e.g. `"3.13"`). Ensures the runtime matches what your code expects.

- **`graphs`** — **Mapping from graph ID to the compiled graph**. Each entry is `"graph_id": "module.path:attribute"` (e.g. `"simple_agent": "app.graphs.simple_agent:graph"`). The platform **imports that module and uses the named object** (a compiled `StateGraph`) as the runnable graph. This is how the server discovers which graphs exist and can serve them by ID (e.g. in the runs API).

- **`assistants`** — **Named entry points** for Studio and the API. Each assistant has a unique id, a `graph_id` (which graph it uses), plus `name` and `description` for the UI. The platform uses this to list “assistants” in LangGraph Studio and to route runs: when you invoke an assistant, the server runs the graph referenced by `graph_id`. You can have multiple assistants pointing at the same graph (e.g. with different configs) or one assistant per graph.

In short: the platform **reads `langgraph.json`** to know which graphs to load (from `graphs`), what to install (`dependencies`), what env to use (`env`), and what to expose as assistants (`assistants`), then **serves those graphs** via the Agent Server API and Studio. 

#### Activity #1:

Create your own agent graph! Build a new graph in `app/graphs/` with a custom evaluation node (e.g., a vibe checker, a fact verifier, a summarizer — get creative!). Register it in `langgraph.json`, serve it with `uv run langgraph dev`

##### Answer:

# Ship 🚢

- The completed notebook.
- 5min. Loom Video

# Share 🚀

- Walk through your notebook and explain what you've completed in the Loom video
- Make a social media post about your final application and tag @AIMakerspace
- Share 3 lessons learned
- Share 3 lessons not learned

# Submitting Your Homework

### Main Homework Assignment

Follow these steps to prepare and submit your homework:

1. Pull the latest updates from upstream into the main branch of your AIE9 repo:
  - *(You should have completed this process already.)* For your initial repo setup, see [Initial_Setup](https://github.com/AI-Maker-Space/AIE9/tree/main/00_Docs/Prerequisites/Initial_Setup)
    - To get the latest updates from AI Makerspace into your own AIE9 repo, run the following commands:
    ```
    git checkout main
    git pull upstream main
    git push origin main
    ```
2. **IMPORTANT:** Start Cursor from the `15_LangGraph_Platform` folder (you can also use the *File -> Open Folder* menu option of an existing Cursor window)
3. Answer Questions 1 - 2 using the `##### Answer:` markdown cell below them in the README
4. Complete Activity #1 in the README
5. Add, commit and push your modified files to your GitHub repository.

When submitting your homework, provide:

- Your Loom video link
- The GitHub URL to the `15_LangGraph_Platform` folder on your assignment branch

