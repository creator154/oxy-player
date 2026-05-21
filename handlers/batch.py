from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from main import app


@app.on_callback_query(filters.regex("batches"))
async def batch_menu(client, query):
    buttons = InlineKeyboardMarkup([
        [InlineKeyboardButton("Yakeen NEET 2027", callback_data="batch_1")]
    ])

    await query.message.edit_text(
        "📚 Select Batch",
        reply_markup=buttons
    )
