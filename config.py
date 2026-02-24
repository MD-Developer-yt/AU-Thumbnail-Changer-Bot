import os
import random
# Bot Configuration
API_TOKEN = os.environ.get("API_TOKEN", "")
# MongoDB
MONGO_URL = os.environ.get("MONGO_URL", "")
DB_NAME = "thumbnail_bot"
# Owner/Admin
OWNER_ID = int(os.environ.get("OWNER_ID", ""))
# UI URLs - Multiple images that rotate randomly
# Use DIRECT image URLs (https://i.ibb.co/...) not page URLs (https://ibb.co/...)
START_PICS = [
    "https://files.catbox.moe/hh2ubq.jpg",
    # Add more direct image URLs here
]
CHANNEL_URL = os.environ.get("CHANNEL_URL", "https://t.me/cantarellabots")
DEV_URL = os.environ.get("DEV_URL", "https://t.me/cantarella_wuwa")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "0"))  # e.g., -100xxxxxxxxxxxx

def get_random_pic() -> str:
    """Get a random image from START_PICS."""
    if START_PICS:
        return random.choice(START_PICS)
    return None
