from pyrogram import filters
from main import app


@app.on_message(filters.private & filters.text)
async def login_handler(client, message):
    text = message.text

    if "eyJ" in text:
        await message.reply_text("✅ Token Saved Successfully")
