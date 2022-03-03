from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from server.database import (
    add_asset,
    delete_asset,
    retrieve_asset,
    retrieve_assets,
    update_asset,
)
from server.models.asset import (
    ErrorResponseModel,
    ResponseModel,
    AssetSchema,
    UpdateAssetModel,
)

router = APIRouter()

@router.post("/", response_description="Asset data added into the database")
async def add_asset_data(asset: AssetSchema = Body(...)):
    asset = jsonable_encoder(asset)
    new_asset = await add_asset(asset)
    return ResponseModel(new_asset, "Asset added successfully.")

@router.get("/", response_description="Assets retrieved")
async def get_assets():
    assets = await retrieve_assets()
    if assets:
        return ResponseModel(assets, "Assets data retrieved successfully")
    return ResponseModel(assets, "Empty list returned")


@router.get("/{id}", response_description="Asset data retrieved")
async def get_asset_data(id):
    asset = await retrieve_asset(id)
    if asset:
        return ResponseModel(asset, "Asset data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "Asset doesn't exist.")

@router.put("/{id}")
async def update_asset_data(id: str, req: UpdateAssetModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_asset = await update_asset(id, req)
    if updated_asset:
        return ResponseModel(
            "Asset with ID: {} name update is successful".format(id),
            "Asset name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the asset data.",
    )

@router.delete("/{id}", response_description="Asset data deleted from the database")
async def delete_asset_data(id: str):
    deleted_asset = await delete_asset(id)
    if deleted_asset:
        return ResponseModel(
            "Asset with ID: {} removed".format(id), "Asset deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "Asset with id {0} doesn't exist".format(id)
    )
