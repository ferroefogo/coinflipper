import os
from dotenv.main import load_dotenv

load_dotenv()

PREFIX = "/"
BOT_NAME = "COINFLIPPER"
BOT_TOKEN = os.getenv("TOKEN")
GUILD_ID = int(os.getenv("GUILD_ID"))