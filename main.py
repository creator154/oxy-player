from pyrogram import Client
from config import *

app = Client(
    "course-bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

import handlers.start
import handlers.login
import handlers.batch
import handlers.extractor
import handlers.uploader
import handlers.live
import handlers.admin

print("Bot Started")

app.run()
