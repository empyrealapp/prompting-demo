import datetime


async def get_current_time() -> str:
    """return popular articles from the New York Times"""

    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
