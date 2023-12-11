from fastapi import APIRouter, FastAPI, HTTPException, status
from models import PostLog, GetLog, GetLogData
import psycopg2
import uuid
import time
import os



app = FastAPI()
app_router = APIRouter()


db_params = {
    "dbname": "mtech",
    "user": "mtech",
    "password": "mtech_321",
    "host": "db",
    "port": "5432",
}


# Подклбчение к бд Postgres
conn = psycopg2.connect(**db_params)
cur = conn.cursor()


@app_router.get("/api/data")
async def get_data() -> list:
    try:
        query = """SELECT uuid4, created, ip, method, uri, status_code 
                   FROM get_log AS A INNER JOIN get_log_data AS B ON A.log_id = B.id;
                """ 
        cur.execute(query)
        data = cur.fetchall()
        return_list = []
        # Формирую список с записями
        for i in data:
            data_dict = {}
            data_dict["id"] = i[0]
            # Дату надо привести в нормальный вид
            data_dict["created"] = i[1]
            data_dict["log"] = {
                "ip": i[2],
                "method": i[3],
                "uri": i[4],
                "status_code": i[5],
            }
            return_list.append(data_dict)
        
    except:
        pass
    return return_list



@app_router.post("/api/data", status_code=201)
async def post_data(log: PostLog) -> dict:

    try:
        # Парсинг
        log = str(log)[5:].replace("'", "").split()
        # Запись в словарь
        log = {"ip": log[0][1:-1],
            "method": log[1][1:-1],
            "uri": log[2][1:-1],
            "status_code": log[3][1:-1]}
        
        # Валидация
        GetLogData(**log)
    
        # Вставляю в лог
        cur.execute("""INSERT INTO get_log_data (ip, method, uri, status_code)
                        VALUES (%s, %s, %s, %s) RETURNING id;""", 
                        (log["ip"], log["method"], log["uri"], log["status_code"]))
        inserted_id = int(cur.fetchone()[0])
        cur.execute("""INSERT INTO get_log (uuid4, log_id) VALUES (%s, %s);""", (str(uuid.uuid4()), inserted_id))

        conn.commit()
        
        # Тут будет добавление в базу данных
        return {"message": "Лог сохранен"}
        
    except:
        raise HTTPException(status_code=status.HTTP_418_IM_A_TEAPOT, detail="Что-то пошло не так")


app.include_router(app_router)
