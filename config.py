import os
import random
# Bot Configuration
API_TOKEN = os.environ.get("API_TOKEN", "23639272")
# MongoDB
MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srv://amimeinhindi:n2PMMs07YTC1Unpg@cluster0.l6wffte.mongodb.net/?appName=Cluster0")
DB_NAME = "thumbnail_bot"
# Owner/Admin
OWNER_ID = int(os.environ.get("OWNER_ID", "7284759394"))
# UI URLs - Multiple images that rotate randomly
# Use DIRECT image URLs (https://i.ibb.co/...) not page URLs (https://ibb.co/...)
START_PICS = [
    "https://files.catbox.moe/hh2ubq.jpg",
    # Add more direct image URLs here
]
CHANNEL_URL = os.environ.get("CHANNEL_URL", "https://t.me/Anime_UpdatesAU")
DEV_URL = os.environ.get("DEV_URL", "https://t.me/Mr_Mohammed_29")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "0"))  # e.g., -100xxxxxxxxxxxx

def get_random_pic() -> str:
    """Get a random image from START_PICS."""
    if START_PICS:
        return random.choice(START_PICS)
    return None
