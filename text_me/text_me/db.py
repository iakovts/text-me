import asyncio

from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi

from .settings import config


# uri = (f'mongodb://{config.get("user")}:{config.get("password")}'
#        f'@{config.get("host")}:{config.get("port")}/{config.get("database")}')
client = AsyncIOMotorClient(
        host=config["mongodb"].get("host"),
        port=int(config["mongodb"].get("port")),
        username=config["mongodb"].get("username"),
        password=config["mongodb"].get("password")
)
db = getattr(client, f"{config['mongodb']['database']}")
post_collection = db.post_collection
import pdb; pdb.set_trace()


async def write_post(data: dict[str, str]):
    document = {"from": data["from"], "text": data["user_text"]}
    result = await post_collection.insert_one(document)
    # result = await db.insert_one(document)
    return result.inserted_id


async def find_by_id(ObjID):
    document = await db.post_collection.find_one(ObjID)
    return document


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


if __name__ == "__main__":
    asyncio.run(test_db())
