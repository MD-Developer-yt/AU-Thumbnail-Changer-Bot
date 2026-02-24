[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&pause=1000&color=36BCF7F1&width=435&lines=Welcome+To+MD+Developer+Yt+Github;It+is+Amazing+AU+Thumbnail+Changer+Bot;Bot+is+Made+By+Mohammed)](https://git.io/typing-svg)

<p align="center">
  <a href="https://www.python.org/" target="_blank">
    <img src="https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python 3"/>
  </a>
  <a href="https://docs.pyrogram.org/" target="_blank">
    <img src="https://img.shields.io/badge/Framework-Pyrogram-brightgreen?style=for-the-badge&logo=pyrogram&logoColor=white" alt="Pyrogram"/>
  </a>
  <a href="https://t.me/Anime_UpdatesAU" target="_blank">
    <img src="https://img.shields.io/badge/Developer-Mohammed-purple?style=for-the-badge&logo=telegram&logoColor=white" alt="Developer"/>
  </a>
  <a href="https://t.me/AU_Bot_Discussion" target="_blank">
    <img src="https://img.shields.io/badge/Support-Group-blueviolet?style=for-the-badge&logo=telegram&logoColor=white" alt="Support Group"/>
  </a>
</p>

---

## 🛠 Features

<ul>
<li>🖼️ <b>Custom Thumbnails</b> – Set your own cover for videos (PNG, JPG, JPEG)</li>
<li>⚡ <b>Fast Processing</b> – Instant video forwarding</li>
<li>🔄 <b>Rotating Images</b> – Dynamic start images</li>
<li>👥 <b>User Database</b> – MongoDB storage</li>
<li>🏆 <b>Leaderboard</b> – Track top users</li>
<li>🛡️ <b>Admin Controls</b> – Ban, Broadcast, Stats</li>
<li>📏 <b>Recommended Size</b> – 1280x720 px, under 2 MB, Ratio 16:9 or 16:8</li>
<li>🐍 <b>Python 3</b> – Latest version</li>
<li>⚡ <b>Pyrogram</b> – Lightweight Telegram API framework</li>
</ul>

---

## 🖼️ Thumbnail Recommendations

<div style="background-color:#f0f8ff; border-left:5px solid #1e90ff; padding:12px; margin:10px 0; border-radius:5px;">
<b>✅ Recommended:</b><br>
• Size: <b>1280x720 px</b><br>
• Maximum file size: <b>2 MB</b><br>
• Aspect Ratio: <b>16:9 or 16:8</b><br>
• Supported formats: <b>PNG, JPG, JPEG</b><br>
<b>💡 Tip:</b> Using the recommended size ensures thumbnails display perfectly on Telegram.
</div>

---

<details>
<summary><h3>
- <b> ᴅᴇᴘʟᴏʏᴍᴇɴᴛ ᴍᴇᴛʜᴏᴅs </b>
</h3></summary>
<h3 align="center">
    ─「 ᴅᴇᴩʟᴏʏ ᴏɴ ʜᴇʀᴏᴋᴜ 」─
</h3>

<p align="center"><a href="https://heroku.com/deploy?template=https://github.com/Codeflix-Bots/ProRenameBot">
  <img src="https://www.herokucdn.com/deploy/button.svg" alt="Deploy On Heroku">
</a></p>
<h3 align="center">
    ─「 ᴅᴇᴩʟᴏʏ ᴏɴ ᴋᴏʏᴇʙ 」─
</h3>
<p align="center"><a href="https://app.koyeb.com/deploy?type=git&repository=github.com/Codeflix-Bots/ProRenameBot&branch=main&name=ProRenameBot">
  <img src="https://www.koyeb.com/static/images/deploy/button.svg" alt="Deploy On Koyeb">
</a></p>
<h3 align="center">
    ─「 ᴅᴇᴩʟᴏʏ ᴏɴ ʀᴇɴᴅᴇʀ 」─
</h3>
<p align="center"><a href="https://render.com/deploy?repo=https://github.com/Codeflix-Bots/ProRenameBot">
<img src="https://render.com/images/deploy-to-render-button.svg" alt="Deploy to Render">
</a></p>
<h3 align="center">
    ─「 ᴅᴇᴩʟᴏʏ ᴏɴ ᴠᴘs 」─
</h3>
<p>
<pre>
💻 Local
  pip install -r requirements.txt
python main.py
</pre>
</p>
</details>

### Steps to Deploy:

1. Fork this repo
2. Create a new App / Service on the chosen platform.  
3. Connect your GitHub repository.  
4. Add environment variables / config vars.  
5. Deploy and start your bot.  

💡 **Tip:** Make sure `API_TOKEN (Bot Token)`, `MONGO_URL`, and `OWNER_ID` are set before running the bot.

---

## ⚙️ Configuration

These are the **environment variables** required to run Bot:

<table>
  <thead>
    <tr>
      <th>Variable</th>
      <th>Description</th>
      <th>Required</th>
      <th>Example / Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>API_TOKEN</code></td>
      <td>Bot token from <a href="https://t.me/BotFather" target="_blank">@BotFather</a></td>
      <td>✅</td>
      <td><code>123456789:ABCDEFxyz1234567890</code></td>
    </tr>
    <tr>
      <td><code>MONGO_URL</code></td>
      <td>MongoDB connection string for storing user data</td>
      <td>✅</td>
      <td><code>mongodb+srv://user:pass@cluster0.mongodb.net/dbname</code></td>
    </tr>
    <tr>
      <td><code>OWNER_ID</code></td>
      <td>Your Telegram user ID (numeric)</td>
      <td>✅</td>
      <td><code>123456789</code></td>
    </tr>
    <tr>
      <td><code>LOG_CHANNEL</code></td>
      <td>Channel ID for logs (optional)</td>
      <td>❌</td>
      <td><code>-1001234567890</code></td>
    </tr>
    <tr>
      <td><code>CHANNEL_URL</code></td>
      <td>Public URL for Telegram channel (optional, join button)</td>
      <td>❌</td>
      <td><a href="https://t.me/Anime_UpdatesAU" target="_blank">https://t.me/Anime_UpdatesAU</a></td>
    </tr>
    <tr>
      <td><code>DEV_URL</code></td>
      <td>Telegram URL of the developer (optional)</td>
      <td>❌</td>
      <td><a href="https://t.me/Mohammed" target="_blank">https://t.me/Mohammed</a></td>
    </tr>
  </tbody>
</table>

---

---

## 🤖 Bot Commands

| Command | Description |
|---------|------------|
| `/start` | Start the bot and get welcome message |
| `/users` | (Admin) View all users in the database |
| `/topleaderboard` | (Admin) Shows the top users by activity |
| `/broadcast` | (Admin) Send a message to all users |
| `/ban` | (Admin) Ban a specific user |
| `/unban` | (Admin) Unban a user |
| `/add_admin` | (Owner) Add a new admin |
| `/remove_admin` | (Owner) Remove an admin |
| `/set_thumbnail` | Upload or change a custom thumbnail |
| `/view_thumbnail` | View the current thumbnail |
| `/remove_thumbnail` | Remove the current thumbnail |

<p align="center">
  💡 Tip: Copy these commands and send to your bot to test 
</p>
---

「 ɴᴏᴛᴇ 」
ɪᴍᴘᴏʀᴛɪɴɢ ᴛʜɪs ʀᴇᴘᴏ ɪɴsᴛᴇᴀᴅ ᴏғ ғᴏʀᴋɪɴɢ ɪs sᴛʀɪᴄᴛʟʏ ᴘʀᴏʜɪʙɪᴛᴇᴅ 🚫 ᴋɪɴᴅʟʏ ғᴏʀᴋ ᴀɴᴅ ᴇᴅɪᴛ ᴀs ʏᴏᴜʀ ᴡɪsʜ (ᴍᴜsᴛ ɢɪᴠᴇ ᴄʀᴇᴅɪᴛs ғᴏʀ ᴅᴇᴠs) 🙃
ɪғ ʏᴏᴜ ғɪɴᴅ ᴀɴʏ ʙᴜɢs ᴏʀ ᴇʀʀᴏʀs, ʀᴇᴘᴏʀᴛ ɪᴛ ᴛᴏ ᴛʜᴇ ᴅᴇᴠᴇʟᴏᴘᴇʀ.

═★═★═★═ **🏆 Credits** ═★═★═★═  

- Developer: <a href="https://t.me/Mr_Mohammed_29"><b>ᴍᴏʜᴀᴍᴍᴇᴅ</b></a>  
- Framework: <a href="https://docs.pyrogram.org/"><b>ᴘʏʀᴏɢʀᴀᴍ</b></a>  

---

---

## Fork and ⭐ this repo 
<p align="center">
  If you like this bot, give it a ⭐ on GitHub to support the project!  
  <a href="https://github.com/MD-Developer-yt/AU-Thumbnail-Changer-Bot" target="_blank">
  </a>
</p>
# ᴅᴏɴ'ᴛ ʀᴇᴍᴏᴠᴇ ᴍʏ ᴄʀᴇᴅɪᴛ...
---

## 🛡 Badges

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.14+-blue" alt="Python">
  <img src="https://img.shields.io/badge/Pyrogram-v2.0-green" alt="Pyrogram">
  <img src="https://img.shields.io/badge/Telegram-Bot-blueviolet" alt="Telegram">
</p>

---
