from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_URL

mongo = AsyncIOMotorClient(MONGO_URL)
db = mongo["pw_bot"]
users = db.users


async def save_token(user_id, token):
    await users.update_one(
        {"user_id": user_id},
        {"$set": {"token": token}},
        upsert=True
    )


async def get_token(user_id):
    data = await users.find_one({"user_id": user_id})

    if data:
        return data.get("token")

    return None
