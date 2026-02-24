FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "main.py"]

#Don't Remove Credits 
#Supports Group @AU_Bot_Discussion 
#Telegram Channel @Anime_UpdatesAU
#Developer @Mr_Mohammed_29
