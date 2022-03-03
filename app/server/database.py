import os
from dotenv import load_dotenv
from bson.objectid import ObjectId
from datetime import datetime

import motor.motor_asyncio


load_dotenv()
MONGO_URL = os.getenv('DB_URI')
CLIENT_PEM = 'app\server\certs\X509-cert-100259875534053013.pem'

client = motor.motor_asyncio.AsyncIOMotorClient(
    MONGO_URL,
    tls=True,
    tlsCertificateKeyFile=CLIENT_PEM)
db = client.deskioDB

companies_col =  db.get_collection("companies")
assets_col =  db.get_collection("assets")


def asset_helper(asset) -> dict:
    return {
        "id": str(asset["_id"]),
        "companyName": asset["companyName"],
        "type": asset["type"],
        "friendlyName": asset["friendlyName"],
        "slug": asset["slug"],
        "date_added": asset["date_added"],
        "date_updated": asset["date_updated"],
    }

# Retrieve all students present in the database
async def retrieve_assets():
    assets = []
    async for asset in assets_col.find():
        assets.append(asset_helper(asset))
    return assets


# Add a new student into to the database
async def add_asset(asset_data: dict) -> dict:
    asset_data["date_added"] = datetime.utcnow()
    asset_data["date_updated"] = datetime.utcnow()
    asset = await assets_col.insert_one(asset_data)
    new_asset = await assets_col.find_one({"_id": asset.inserted_id})
    return asset_helper(new_asset)


# Retrieve a student with a matching ID
async def retrieve_asset(id: str) -> dict:
    asset = await assets_col.find_one({"_id": ObjectId(id)})
    if asset:
        return asset_helper(asset)


# Update a student with a matching ID
async def update_asset(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    asset = await assets_col.find_one({"_id": ObjectId(id)})
    if asset:
        data["date_updated"] = datetime.utcnow()
        updated_asset = await assets_col.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if update_asset:
            return True
        return False


# Delete a student from the database
async def delete_asset(id: str):
    asset = await assets_col.find_one({"_id": ObjectId(id)})
    if asset:
        await assets_col.delete_one({"_id": ObjectId(id)})
        return True
