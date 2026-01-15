<p align = "center" draggable="false" ><img src="https://github.com/AI-Maker-Space/LLM-Dev-101/assets/37101144/d1343317-fa2f-41e1-8af1-1dbb18399719"
     width="200px"
     height="auto"/>
</p>

<h1 align="center" id="heading">Session 1: Introduction and Vibe Check</h1>

### [Quicklinks](https://github.com/AI-Maker-Space/AIE9/tree/main/00_AIM_Quicklinks)

| 📰 Session Sheet | ⏺️ Recording     | 🖼️ Slides        | 👨‍💻 Repo         | 📝 Homework      | 📁 Feedback       |
|:-----------------|:-----------------|:-----------------|:-----------------|:-----------------|:-----------------|
| [Vibe Check!](https://github.com/AI-Maker-Space/AIE9/blob/main/00_Docs/Session_Sheets/01_Vibe_Check.md) |[Recording!](https://drive.google.com/file/d/1Rsmm0Hld3WFHRxhZpEDLN_JREQ43yhwu/view?usp=drive_link) | [Session 1 Slides](https://www.canva.com/design/DAG-EBzN2PQ/gE9-Uma217yych4M7GCjSw/edit?utm_content=DAG-EBzN2PQ&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton) | You are here! | [Session 1 Assignment: Vibe Check](https://forms.gle/NeN59bCLdtXvwzVJ9) | [Feedback 1/13](https://forms.gle/1im4nmYK9cW9MFEk6)

## 🏗️ How AIM Does Assignments

> 📅 **Assignments will always be released to students as live class begins.** We will never release assignments early.

Each assignment will have a few of the following categories of exercises:

- ❓ **Questions** – these will be questions that you will be expected to gather the answer to! These can appear as general questions, or questions meant to spark a discussion in your breakout rooms!

- 🏗️ **Activities** – these will be work or coding activities meant to reinforce specific concepts or theory components.

- 🚧 **Advanced Builds (optional)** – Take on a challenge! These builds require you to create something with minimal guidance outside of the documentation. Completing an Advanced Build earns full credit in place of doing the base assignment notebook questions/activities.

### Main Assignment

In the following assignment, you are required to take the app that you created for the AIE9 challenge (from [this repository](https://github.com/AI-Maker-Space/The-AI-Engineer-Challenge)) and conduct what is known, colloquially, as a "vibe check" on the application.

You will be required to submit a link to your GitHub, as well as screenshots of the completed "vibe checks" through the provided Google Form!

> NOTE: This will require you to make updates to your personal class repository, instructions on that process can be found [here](https://github.com/AI-Maker-Space/AIE9/tree/main/00_Initial_Setup)!


#### A Note on Vibe Checking

>"Vibe checking" is an informal term for cursory unstructured and non-comprehensive evaluation of LLM-powered systems. The idea is to loosely evaluate our system to cover significant and crucial functions where failure would be immediately noticeable and severe.
>
>In essence, it's a first look to ensure your system isn't experiencing catastrophic failure.

---

#### 🏗️ Activity #1: General Vibe Checking Evals

Please evaluate your system on the following questions:

1. Explain the concept of object-oriented programming in simple terms to a complete beginner.
    - Aspect Tested: The LLMs correctness and ability to adapt its answer to a specific target audience is whats being tested. My LLM is build to answer space related questions or topics, and that’s specified in the prompt. So its response was: I only answer space-related questions. Please ask about planets, rockets, black holes, telescopes, or space exploration.
2. Read the following paragraph and provide a concise summary of the key points…
    - Aspect Tested: Can the LLM summarize important info from a paragraph of text. Can it decide what actually is important? My app would only attempt to provide a summary if the paragraph was space related. 
3. Write a short, imaginative story (100–150 words) about a robot finding friendship in an unexpected place.
    - Aspect Tested: Is the LLM creative within the criteria being specified but also can it fall within the restraints enforced (100-150 words). My chatbot was able to generate a story about the robot finding a friend (in space of course) and it generated the story in 127 words!
4. If a store sells apples in packs of 4 and oranges in packs of 3, how many packs of each do I need to buy to get exactly 12 apples and 9 oranges?
    - Aspect Tested: Can the LLM problem solve and perform basic mathematical operations. My chatbot rejected question because its not related to space
5. Rewrite the following paragraph in a professional, formal tone…
    - Aspect Tested: Testing the LLMs ability to adjust to a specific target audience. My chatbot allows the user to follow up with a paragraph but will reject it if it’s not space related. When giving it a space related paragraph I didn’t really see any significant changes in the tone

#### ❓Question #1:

Do the answers appear to be correct and useful?
##### ✅ Answer:
Yes, the answers are extremely useful. It’s good to understand how the LLM behaves, whether it can follow instructions and remain within constraints. Also its good to understand if it has the ability to cater to specific audiences. No answer was technically incorrect so far and if the question asked was not a space related question it did a decent job of identifying that and notifying the user

---

#### 🏗️ Activity #2: Personal Vibe Checking Evals (Your Assistant Can Answer)

Now test your assistant with personal questions it should be able to help with. Try prompts like:

- "Help me think through the pros and cons of [enter decision you're working on making]."
- "What are the pros and cons of [job A] versus [job B] as the next step in my career?"
- "Draft a polite follow-up [email, text message, chat message] to a [enter person details] who hasn't responded."
- "Help me plan a birthday surprise for [person]."
- "What can I cook with [enter ingredients] in fridge."

##### Your Prompts and Results:
1. Prompt: Draft a polite follow-up email to my friend Danny who hasn't responded about starting a colony on mars
   - Result: It did generate a follow up email with an appropriate tone a follow up email should have. This purpose of this chat bot is not to write emails though
2. Prompt: Help me plan a birthday surprise for ELON MUSK
   - Result: It ended up generating a plan to throw a space themed birthday party for Elon. I also changed the name from Elon Musk to Bill Clinton and it still generated a space themed birthday but it also added a blurb on how it only answers space related questions. Its not designed as a birthday chatbot
3. Prompt: Help me think through the pros and cons of starting a colony on Mars vs staying on earth. Explain both sides as if I'm a child

   - Result: It was able to explain pros and cons of each; the tone it used was very simple but “child” really depends on the age. I do think a child that’s able to read this can understand it


#### ❓Question #2:

Are the vibes of this assistant's answers aligned with your vibes? Why or why not?
##### ✅ Answer:
Not yet. If I ask it a completely irrevlevant question and add a couple words about space it still attempts to answer it. It needs more strict guardrails
---

#### 🏗️ Activity #3: Personal Vibe Checking Evals (Requires Additional Capabilities)

Now test your assistant with questions that would require capabilities beyond basic chat, such as access to external tools, APIs, or real-time data. Try prompts like:

- "What does my schedule look like tomorrow?"
- "What time should I leave for the airport?"

##### Your Prompts and Results:
1. Prompt: What spacecraft are en route to Mars today?
   - Result: I don’t know the real-time status today. As of Oct 2024, none were en route; the next planned were NASA’s ESCAPADE twin orbiters and JAXA’s MMX (to the Mars system), both awaiting launch. For up-to-date status, check their mission pages.
2. Prompt: What was the most recent SpaceX launch outcome?
   - Result: I don’t know. For the latest outcome, check SpaceX’s X feed (@SpaceX), spacex.com/launches, NextSpaceflight, or Spaceflight Now’s launch log.

#### ❓Question #3:

What are some limitations of your application?
##### ✅ Answer: 
It struggles answering questions that involve getting realtime information, it also seems to give inconsistent answers (like swapping Musk for Clinton). Its also pretty slow and could use some optimizations

---

This "vibe check" now serves as a baseline, of sorts, to help understand what holes your application has.

### 🚧 Advanced Build (OPTIONAL):

Please make adjustments to your application that you believe will improve the vibe check you completed above, then deploy the changes to your Vercel domain [(see these instructions from your Challenge project)](https://github.com/AI-Maker-Space/The-AI-Engineer-Challenge/blob/main/README.md) and redo the above vibe check.

> NOTE: You may reach for improving the model, changing the prompt, or any other method.

#### 🏗️ Activity #1
##### Adjustments Made:
- _describe adjustment(s) here_

##### Results:
1. _Comment here how the change(s) impacted the vibe check of your system_
2.
3.
4.
5.


## Submitting Your Homework
### Main Assignment
Follow these steps to prepare and submit your homework:
1. Pull the latest updates from upstream into the main branch of your AIE9 repo:
    - For your initial repo setup see [00_Initial_Setup](https://github.com/AI-Maker-Space/AIE9/tree/main/00_Initial_Setup)
    - To get the latest updates from AI Makerspace into your own AIE9 repo, run the following commands:
    ```
    git checkout main
    git pull upstream main
    git push origin main
    ```
2. **IMPORTANT:** Start Cursor from the `01_Prototyping_Best_Practices_and_Vibe_Check` folder (you can also use the _File -> Open Folder_ menu option of an existing Cursor window)
3. Edit this `README.md` file (the one in your `AIE9/01_Prototyping_Best_Practices_and_Vibe_Check` folder)
4. Complete all three Activities:
    - **Activity #1:** Evaluate your system using the general vibe checking questions and define the "Aspect Tested" for each
    - **Activity #2:** Test your assistant with personal prompts it should be able to answer
    - **Activity #3:** Test your assistant with prompts requiring additional capabilities
5. Provide answers to all three Questions (`❓Question #1`, `❓Question #2`, `❓Question #3`)
6. Add, commit and push your modified `README.md` to your origin repository's main branch.

When submitting your homework, provide the GitHub URL to your AIE9 repo.

### The Advanced Build:
1. Follow all of the steps (Steps 1 - 6) of the Main Assignment above
2. Document what you changed and the results you saw in the `Adjustments Made:` and `Results:` sections of the Advanced Build
3. Add, commit and push your additional modifications to this `README.md` file to your origin repository.

When submitting your homework, provide the following on the form:
+ The GitHub URL to your AIE9 repo.
+ The public Vercel URL to your updated Challenge project on your AIE9 repo.
