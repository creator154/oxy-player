from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def main_buttons():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("📚 Batches", callback_data="batches")],
        [InlineKeyboardButton("🎥 Live", callback_data="live")]
    ])
