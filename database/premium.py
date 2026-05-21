from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_URL

mongo = AsyncIOMotorClient(MONGO_URL)
db = mongo["pw_bot"]
premium = db.premium


async def add_premium(user_id, days):
    await premium.update_one(
        {"user_id": user_id},
        {"$set": {"days": days}},
        upsert=True
    )


async def is_premium(user_id):
    data = await premium.find_one({"user_id": user_id})

    if data:
        return True

    return False
