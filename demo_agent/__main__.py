import asyncio
import random
from typing import Optional

import click
from dotenv import load_dotenv

from .agent import DemoAgent


@click.group()
def cli() -> None:
    """Demo Agent CLI"""
    load_dotenv()


@cli.command()
@click.option("-o", "--omit-conversation-history", is_flag=True, default=False)
def run(omit_conversation_history: bool = False) -> None:
    """
    Run the Demo Agent

    If you pass -o to the command, the agent will not use the conversation history.
    """

    agent = DemoAgent(use_conversation_history=not omit_conversation_history)
    agent.run_sync()
    return None


@cli.command()
@click.argument("message", type=str)
def ask(message: str) -> None:
    """Ask the Demo Agent a question"""
    load_dotenv()
    agent = DemoAgent()
    answer = asyncio.run(agent.answer(message))
    return click.echo(answer)


@cli.command()
@click.option("--topic", type=str)
@click.option("--tweet-length", type=Optional[int], default=None)
def tweet(topic: str, tweet_length: int | None) -> None:
    """Compose a tweet about the given topic"""
    load_dotenv()
    agent = DemoAgent()

    # varies the length of the tweet so it's not always the same length
    if not tweet_length:
        tweet_length = random.randint(120, 280)

    question = (
        f"Respond to the following topic with any size less than {tweet_length} characters, with NO emojis:"
        + topic
    )
    answer = asyncio.run(agent.answer(question))

    return click.echo(answer)


if __name__ == "__main__":
    cli()
