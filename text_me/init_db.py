import motor 
import asyncio

from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi

from text_me.settings import config 


# __all__ == ["client"]

client = motor.motor_asyncio.AsyncIOMotorClient(config.get("host", "localhost"), config.get("port", 27017))
db = client.posts
post_collection = db.collection

async def write_post(data: dict[str, str]):
    document = {"from": data["from"], "text": data["text"]}
    result = await db.post_collection.insert_one(document)
    return result

async def find_by_id(ObjID):
    document = await db.post_collection.find_one(ObjID)
    return document


async def ping_server():
  # Replace the placeholder with your Atlas connection string
  uri = config.get("host", "localhost")
  # Set the Stable API version when creating a new client
  client = AsyncIOMotorClient(uri, server_api=ServerApi('1'))

  # Send a ping to confirm a successful connection
  try:
      await client.admin.command('ping')
      print("Pinged your deployment. You successfully connected to MongoDB!")
  except Exception as e:
      print(e)
      
async def test_server():
    # asyncio.run(ping_server())
    inserted_id = await write_post({"from": "me", "text": "bla"})
    doc = await find_by_id(inserted_id.inserted_id)
    import pdb; pdb.set_trace()

if __name__ == "__main__":
    asyncio.run(test_server())


