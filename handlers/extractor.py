import aiohttp
from pyrogram import filters
from main import app
from database.users import get_token


@app.on_callback_query(filters.regex("batch_"))
async def extractor(client, query):
    token = await get_token(query.from_user.id)

    if not token:
        return await query.message.reply_text(
            "❌ Login First"
        )

    await query.message.reply_text(
        "⏳ Extracting Videos and PDFs..."
    )

    headers = {
        "authorization": f"Bearer {token}"
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(
            "https://api.classplusapp.com",
            headers=headers
        ) as resp:
            data = await resp.text()

    await query.message.reply_text(
        "✅ Extraction Completed"
    )
