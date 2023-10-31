from fastapi import FastAPI
from dotenv import dotenv_values
from pymongo import MongoClient
from group_routes import router as group_router
from member_routes import router as member_router

config = dotenv_values(".env")

app = FastAPI()

@app.on_event("startup")
def startup_db_client():
    print(config["ATLAS_URI"])
    app.mongodb_client = MongoClient("mongodb+srv://bryanadmin:admin@cluster0.lnlrf4e.mongodb.net/?retryWrites=true&w=majority")
    app.database = app.mongodb_client["kpop_db"]
    print("Connected to the MongoDB database!")

@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()


app.include_router(group_router, tags=["groups"], prefix="/group")
app.include_router(member_router, tags=["members"], prefix="/member")