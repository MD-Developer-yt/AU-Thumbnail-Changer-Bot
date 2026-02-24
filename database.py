from motor.motor_asyncio import AsyncIOMotorClient
from typing import Optional, List, Dict, Any
from config import MONGO_URL, DB_NAME, OWNER_ID
# MongoDB client (initialized in main.py)
client: AsyncIOMotorClient = None
db = None

async def init_db():
    """Initialize MongoDB connection."""
    global client, db
    client = AsyncIOMotorClient(MONGO_URL)
    db = client[DB_NAME]
    
    # Create indexes
    await db.users.create_index("user_id", unique=True)
    await db.admins.create_index("user_id", unique=True)
    
    # Add owner as admin by default
    await add_admin(OWNER_ID)
    print("✅ MongoDB connected")

async def close_db():
    """Close MongoDB connection."""
    global client
    if client:
        client.close()

# ==================== USER FUNCTIONS ====================

async def add_user(user_id: int, username: str = None, first_name: str = None):
    """Add or update a user."""
    await db.users.update_one(
        {"user_id": user_id},
        {
            "$set": {
                "username": username,
                "first_name": first_name
            },
            "$setOnInsert": {
                "user_id": user_id,
                "thumbnail_file_id": None,
                "usage_count": 0,
                "banned": False
            }
        },
        upsert=True
    )

async def get_user(user_id: int) -> Optional[Dict[str, Any]]:
    """Get user data."""
    return await db.users.find_one({"user_id": user_id})

async def get_all_users() -> List[Dict[str, Any]]:
    """Get all users."""
    return await db.users.find().to_list(length=None)

async def get_user_count() -> int:
    """Get total user count."""
    return await db.users.count_documents({})

# ==================== THUMBNAIL FUNCTIONS ====================

async def set_thumbnail(user_id: int, file_id: str):
    """Set user's thumbnail."""
    await db.users.update_one(
        {"user_id": user_id},
        {"$set": {"thumbnail_file_id": file_id}}
    )

async def get_thumbnail(user_id: int) -> Optional[str]:
    """Get user's thumbnail file_id."""
    user = await db.users.find_one({"user_id": user_id})
    return user.get("thumbnail_file_id") if user else None

async def remove_thumbnail(user_id: int) -> bool:
    """Remove user's thumbnail."""
    result = await db.users.update_one(
        {"user_id": user_id},
        {"$set": {"thumbnail_file_id": None}}
    )
    return result.modified_count > 0

# ==================== USAGE TRACKING ====================

async def increment_usage(user_id: int):
    """Increment user's usage count."""
    await db.users.update_one(
        {"user_id": user_id},
        {"$inc": {"usage_count": 1}}
    )

async def get_leaderboard(limit: int = 10) -> List[Dict[str, Any]]:
    """Get top users by usage count."""
    return await db.users.find(
        {"usage_count": {"$gt": 0}}
    ).sort("usage_count", -1).limit(limit).to_list(length=limit)

# ==================== BAN FUNCTIONS ====================

async def ban_user(user_id: int) -> bool:
    """Ban a user."""
    result = await db.users.update_one(
        {"user_id": user_id},
        {"$set": {"banned": True}}
    )
    return result.modified_count > 0

async def unban_user(user_id: int) -> bool:
    """Unban a user."""
    result = await db.users.update_one(
        {"user_id": user_id},
        {"$set": {"banned": False}}
    )
    return result.modified_count > 0

async def is_banned(user_id: int) -> bool:
    """Check if user is banned."""
    user = await db.users.find_one({"user_id": user_id})
    return user.get("banned", False) if user else False

# ==================== ADMIN FUNCTIONS ====================

async def add_admin(user_id: int):
    """Add an admin."""
    await db.admins.update_one(
        {"user_id": user_id},
        {"$set": {"user_id": user_id}},
        upsert=True
    )

async def remove_admin(user_id: int) -> bool:
    """Remove an admin."""
    if user_id == OWNER_ID:
        return False  # Cannot remove owner
    result = await db.admins.delete_one({"user_id": user_id})
    return result.deleted_count > 0

async def is_admin(user_id: int) -> bool:
    """Check if user is admin."""
    if user_id == OWNER_ID:
        return True
    admin = await db.admins.find_one({"user_id": user_id})
    return admin is not None
  
async def get_all_admins() -> List[int]:
    """Get all admin IDs."""
    admins = await db.admins.find().to_list(length=None)
    return [a["user_id"] for a in admins]
