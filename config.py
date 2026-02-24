import os
import random
# Bot Configuration
API_TOKEN = os.environ.get("API_TOKEN", "8518273836:AAFrIAg5h83ldwocyfSO6Ht0Jukk3GaH3v0") #add your bot token
# MongoDB
MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srv://amimeinhindi:n2PMMs07YTC1Unpg@cluster0.l6wffte.mongodb.net/?appName=Cluster0") #add your MongoDB URL
DB_NAME = "thumbnail_bot"
# Owner/Admin
OWNER_ID = int(os.environ.get("OWNER_ID", "7284759394")) #add your User id
# UI URLs - Multiple images that rotate randomly
# Use DIRECT image URLs (https://i.ibb.co/...) not page URLs (https://ibb.co/...)
START_PICS = [
    "https://graph.org/file/0e77ba48a8b7a3b09296f-362372bee0d84fd217.jpg",
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
#Don't Remove Credits 
#Supports Group @AU_Bot_Discussion 
#Telegram Channel @Anime_UpdatesAU
#Developer @Mr_Mohammed_29
