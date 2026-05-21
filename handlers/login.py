from pyrogram import filters
from main import app
from database.users import save_token


@app.on_message(filters.private & filters.text)
async def login_handler(client, message):
    text = message.text

    if "eyJ" in text:
        await save_token(message.from_user.id, text)

        await message.reply_text(
            "✅ PW Token Saved Successfully"
        )
