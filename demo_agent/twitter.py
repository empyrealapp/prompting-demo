import os
from typing import Any

from tweepy.asynchronous import AsyncClient


async def execute_tweet(content: str, in_reply_to: str | None = None) -> Any:
    """posts a simple tweet"""
    api = AsyncClient(
        os.environ["TWITTER_BEARER_TOKEN"],
        consumer_key=os.environ["TWITTER_CONSUMER_KEY"],
        consumer_secret=os.environ["TWITTER_CONSUMER_SECRET"],
        access_token=os.environ["TWITTER_ACCESS_TOKEN"],
        access_token_secret=os.environ["TWITTER_ACCESS_SECRET"],
    )
    return await api.create_tweet(
        text=content,
        in_reply_to_tweet_id=in_reply_to,
    )
