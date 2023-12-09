from fastapi import APIRouter
from models import PostLog


app = APIRouter()


data_list = []





@app.get("/api/data")
async def get_data() -> list:
    return data_list



@app.post("/api/data")
async def post_data(log: PostLog) -> dict:

    

    log = str(log)[5:].replace("'", "").split()

    log = {"ip": log[0][1:-1],
           "method": log[1][1:-1],
           "uri": log[2][1:-1],
           "status_code": log[3][1:-1]}

    data_list.append(log)


    return {"message": "succesfully added data"}
