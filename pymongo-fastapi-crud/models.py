import uuid
from typing import Optional
from typing import List
from pydantic import BaseModel, Field


class Member(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    name: str = Field(...)
    member_img_url: str = Field(...)
    birthday: str = Field(...)
    birthplace: str = Field(...)
    position: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
                "name": "Seonghwa(성화)",
                "member_img_url": "https://kpopping.com//documents/5a/1/750/Seonghwa-fullBodyPicture(10).webp?v=0be45&quot;",
                "birthday": "birthday",
                "birthplace": "Anyang, Gyeonggi-do",
                "position": "Leader, Rapper, Composer, Center"
            }
        }


class MemberUpdate(BaseModel):
    id: Optional[str]
    name: Optional[str]
    member_img_url: Optional[str]
    birthday: Optional[str]
    birthplace: Optional[str]
    position: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
                "name": "Seonghwa(성화)",
                "member_img_url": "https://kpopping.com//documents/5a/1/750/Seonghwa-fullBodyPicture(10).webp?v=0be45&quot;",
                "birthday": "birthday",
                "birthplace": "Anyang, Gyeonggi-do",
                "position": "Leader, Rapper, Composer, Center"
            }
        }


class Group(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    name: str = Field(...)
    url: str = Field(...)
    group_img_url: str = Field(...)
    members: List[Member] = []

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
                "name": "ATEEZ",
                "url": "https://kpopping.com/profiles/group/ATEEZ",
                "group_img_url": "https://kpopping.com/documents/f9/4/850/ATEEZ-fullPicture(9).webp?v=49eb1&quot;",
                "members": []
            }
        }


class GroupUpdate(BaseModel):
    id: Optional[str]
    name: Optional[str]
    url: Optional[str]
    group_img_url: Optional[str]
    members: Optional[List[Member]]

    class Config:
        schema_extra = {
            "example": {
                "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
                "name": "ATEEZ",
                "url": "https://kpopping.com/profiles/group/ATEEZ",
                "group_img_url": "https://kpopping.com/documents/f9/4/850/ATEEZ-fullPicture(9).webp?v=49eb1&quot;",
                "members": []
            }
        }


