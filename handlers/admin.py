from pyrogram import filters
from main import app


@app.on_message(filters.command("broadcast"))
async def broadcast(client, message):
    await message.reply_text("📢 Broadcast Sent")
