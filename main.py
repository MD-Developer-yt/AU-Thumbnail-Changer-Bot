#Don't Remove Credits 
#Supports Group @AU_Bot_Discussion 
#Telegram Channel @Anime_UpdatesAU
#Developer @Mr_Mohammed_29
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
import asyncio
from flask import Flask
import threading 
#Don't Remove Credits 
#Supports Group @AU_Bot_Discussion 
#Telegram Channel @Anime_UpdatesAU
#Developer @Mr_Mohammed_29
import os
from config import API_TOKEN
from database import init_db, close_db
from plugins import start_router, settings_router, video_router, admin_router
# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(storage=MemoryStorage())
# Register routers
dp.include_router(start_router)
dp.include_router(settings_router)
dp.include_router(video_router)
dp.include_router(admin_router)
# Flask health check server
app = Flask(__name__)
@app.route("/")

def home():
    return "Bot Made By @Anime_Updates"

def run_flask():
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

async def main():
    # Initialize database
    await init_db()
    print("🚀 Bot is starting...")
    
    try:
        await dp.start_polling(bot)
    finally:
        await close_db()

if __name__ == "__main__":
    print(r"""     
████████████████████████
█     Anime_UpdatesAU      █
████████████████████████
      BOT WORKING PROPERLY....
    """)
    print("Starting Bot...")
    threading.Thread(target=run_flask, daemon=True).start()
    asyncio.run(main())
#Don't Remove Credits 
#Supports Group @AU_Bot_Discussion 
#Telegram Channel @Anime_UpdatesAU
#Developer @Mr_Mohammed_29
