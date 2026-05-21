from pyrogram import filters
from main import app


@app.on_message(filters.command("upload"))
async def uploader(client, message):
    await message.reply_text(
        "📤 Upload Started"
    )
