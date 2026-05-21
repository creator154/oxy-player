from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from main import app


@app.on_message(filters.command("start"))
async def start_cmd(client, message):
    buttons = InlineKeyboardMarkup([
        [InlineKeyboardButton("🚀 Login", callback_data="login")],
        [InlineKeyboardButton("📚 Batches", callback_data="batches")],
        [InlineKeyboardButton("🎥 Live Classes", callback_data="live")]
    ])

    await message.reply_photo(
        photo="https://graph.org/file/example.jpg",
        caption="✨ Welcome To Physics Wallah Extractor Bot ✨",
        reply_markup=buttons
    )
