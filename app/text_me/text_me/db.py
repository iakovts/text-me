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

client = AsyncIOMotorClient(config.get("host", "mongo"), int(config.get("port", 27017)), timeoutMS=5000)
db = client.posts
post_collection = db.collection

async def find_max_counter():
    cursor = db.post_collection.find({}, {"_id": 0, "counter": 1}).sort({ "counter": -1 }).limit(1)
    return await cursor.to_list(length=1)

async def write_post(data: dict[str, str]):
    try:
        write_post.counter
    except AttributeError:
        l = await find_max_counter()
        if (len(l) == 0):
            # set to zero if no counter exists
            write_post.counter = 0;
        else:
            # else set to 1 more than the max to be ready for the upcoming insert
            write_post.counter = l[0]["counter"] + 1;

    document = {
        "from": data["from"],
        "text": data["user_text"],
        "datetime": datetime.datetime.now().isoformat(),
        "counter": write_post.counter,
    }
    write_post.counter += 1 # hi mom
    result = await db.post_collection.insert_one(document)
    return result.inserted_id


async def find_by_id(ObjID):
    document = await db.post_collection.find_one(ObjID)
    return document

async def find_all():
    cursor = db.post_collection.find(
            {}, {"from": 1, "text": 1, "_id": 0, "counter": 1}
    ).limit(1000000)
    return await cursor.to_list(length=1000000)


# async def ping_server():
#     # Replace the placeholder with your Atlas connection string
#     uri = config.get("host", "localhost")
#     # Set the Stable API version when creating a new client
#     client = AsyncIOMotorClient(uri, server_api=ServerApi("1"))
# 
#     # Send a ping to confirm a successful connection
#     try:
#         await client.admin.command("ping")
#         print("Pinged your deployment. You successfully connected to MongoDB!")
#     except Exception as e:
#         print(e)


async def test_db():
    inserted_id = await write_post({"from": "me", "text": "bla"})
    doc = await find_by_id(inserted_id)
