from pyrogram import filters
from app import app


@app.on_message(filters.command("start"))
async def start_cmd(client, message):
    await message.reply_text("Bot Working ✅")
