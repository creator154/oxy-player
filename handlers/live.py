from pyrogram import filters
from main import app


@app.on_callback_query(filters.regex("live"))
async def live_handler(client, query):
    await query.message.reply_text(
        "🔴 Live Classes Loaded"
    )
