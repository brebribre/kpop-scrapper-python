from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List

from models import Member, MemberUpdate

router = APIRouter()




@router.post("/", response_description="Insert a new member", status_code=status.HTTP_201_CREATED, response_model=Member)
def create_member(request: Request, member: Member = Body(...)):
    member = jsonable_encoder(member)
    new_member = request.app.database["members"].insert_one(member)
    created_member = request.app.database["members"].find_one(
        {"_id": new_member.inserted_id}
    )

    return created_member


@router.get("/", response_description="List all members", response_model=List[Member])
def list_members(request: Request):
    members = list(request.app.database["members"].find(limit=300))
    return members