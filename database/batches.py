from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_URL

mongo = AsyncIOMotorClient(MONGO_URL)
db = mongo["pw_bot"]
batches = db.batches


async def save_batch(batch_name, batch_slug):
    await batches.update_one(
        {"slug": batch_slug},
        {
            "$set": {
                "name": batch_name,
                "slug": batch_slug
            }
        },
        upsert=True
    )


async def get_batches():
    data = []

    async for x in batches.find():
        data.append(x)

    return data
