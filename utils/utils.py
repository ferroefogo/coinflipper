import re, asyncio
import config

def blockquote(string: str) -> str:
    return re.sub(r"(^|\n)(?!$)", r"\1", string.strip())

def custom_id(view: str) -> str:
    """CREATES A CUSTOM ID FROM THE BOT NAME"""
    return f"{config.BOT_NAME}:{view}"

async def wait(amount):
    """ALLOWS THE BOT TO SLEEP FOR SPECIFIED AMOUNT OF TIME"""
    await asyncio.sleep(amount)




