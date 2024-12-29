## Demo Agent

This is the basic project layout.  It sets up the boilerplate for adding tools to the agents capabilities, and modifying a simple yaml to configure the prompt and initial conversation history for the agent.  The `DemoAgent` is the main agent class that can be modified to change the behavior of the agent.

# QUICKSTART

```bash
pip install -r requirements.txt
```

# Asking questions

You can ask the agent a question using the CLI

```bash
python -m demo_agent ask "what is the meaning of life?"
```


# Interactive Mode

You can also run the agent in interactive mode, which will allow you to ask the agent a question and then it will respond to you.

```bash
python -m demo_agent run
```

# Tweets

You can also compose a tweet about a given topic.

```bash
python -m demo_agent tweet --topic "AI Agent Development"
```


## Updating The Prompts

You can update the demo_agent/prompts.yaml file to change the behavior of the agent.  The prompts are loaded from the yaml file when the agent is initialized.

The system prompt is the main prompt for the agent.  It is a string that is used to set the behavior of the agent.

The conversation history is a list of messages between the user and the agent.  It is used to set the context of the conversation.
