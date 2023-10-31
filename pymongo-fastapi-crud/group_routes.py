from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List

from models import Group, GroupUpdate

router = APIRouter()




@router.post("/", response_description="Insert a new group", status_code=status.HTTP_201_CREATED, response_model=Group)
def create_group(request: Request, group: Group = Body(...)):
    group = jsonable_encoder(group)
    new_group = request.app.database["groups"].insert_one(group)
    created_group = request.app.database["groups"].find_one(
        {"_id": new_group.inserted_id}
    )

    return created_group


@router.get("/", response_description="List all groups", response_model=List[Group])
def list_groups(request: Request):
    groups = list(request.app.database["groups"].find(limit=300))
    return groups


@router.put("/{id}", response_description="Update a group", response_model=Group)
def update_group(id: str, request: Request, group: GroupUpdate = Body(...)):
    group = {k: v for k, v in group.dict().items() if v is not None}
    if len(group) >= 1:
        update_result = request.app.database["groups"].update_one(
            {"_id": id}, {"$set": group}
        )

        if update_result.modified_count == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Group with ID {id} not found")

    if (
        existing_group := request.app.database["groups"].find_one({"_id": id})
    ) is not None:
        return existing_group

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Group with ID {id} not found")