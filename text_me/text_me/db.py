import asyncio
import datetime
from datetime import timedelta



from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi

try:
    from .settings import config
except ImportError:
    from settings import config


datetime_storage = datetime.datetime.now()

client = AsyncIOMotorClient(config.get("host", "localhost"), config.get("port", 27017))
db = client.posts
post_collection = db.collection

async def write_post(data: dict[str, str]):
    post_counter = 0
    # post_counter_uuid = uuid.uuid4()
    document = {
        "from": data["from"],
        "text": data["user_text"],
        "datetime": datetime.datetime.now().isoformat(),
        # "counter_uuid": post_counter_uuid,
        "count": post_counter,
    }
    post_counter += 1
    result = await db.post_collection.insert_one(document)
    return result.inserted_id


async def find_by_id(ObjID):
    document = await db.post_collection.find_one(ObjID)
    return document


async def find_all():
    cursor = db.post_collection.find(
            {}, {"from": 1, "text": 1, "_id": 0, "count": 1}
    ).limit(100)
    return await cursor.to_list(length=100)


async def ping_server():
    # Replace the placeholder with your Atlas connection string
    uri = config.get("host", "localhost")
    # Set the Stable API version when creating a new client
    client = AsyncIOMotorClient(uri, server_api=ServerApi("1"))

    # Send a ping to confirm a successful connection
    try:
        await client.admin.command("ping")
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)


async def test_db():
    inserted_id = await write_post({"from": "me", "text": "bla"})
    doc = await find_by_id(inserted_id)
