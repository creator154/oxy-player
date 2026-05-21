from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_URL

mongo = AsyncIOMotorClient(MONGO_URL)
db = mongo["pw_bot"]
stats = db.stats


async def add_user(user_id):
    await stats.update_one(
        {"user_id": user_id},
        {"$set": {"user_id": user_id}},
        upsert=True
    )


async def total_users():
    return await stats.count_documents({})
