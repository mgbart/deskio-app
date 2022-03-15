from typing import Optional

from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from bson.objectid import ObjectId

class AssetSchema(BaseModel):

    companyName: str = Field(...)
    type: str = Field(...)
    friendlyName: str = Field(...)
    slug: str = Field(...)
    date_added: Optional[datetime]
    date_updated: Optional[datetime]


    class Config:
        schema_extra = {
            "example": {
                "companyName": "Contoso Inc.",
                "type": "MS Surface Hub",
                "friendlyName": "HR Meeting Room Surface Hub",
                "slug": "contoso-hr-meeting-room-device"
            }
        }


class UpdateAssetModel(BaseModel):
    companyName: Optional[str]
    type: Optional[str]
    friendlyName: Optional[str]
    slug: Optional[str]
    date_added: Optional[datetime]
    date_updated: Optional[datetime]

    class Config:
        schema_extra = {
            "example": {
                "id": "abc123xyz",
                "companyName": "Contoso Inc.",
                "type": "MS Surface Hub",
                "friendlyName": "HR Meeting Room Device",
                "companyId": "hij999klm",
                "slug": "contoso-hr-meeting-room-device",
                "date_added": "datetime.utcnow()",
                "date_updated": "datetime.utcnow()"
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
