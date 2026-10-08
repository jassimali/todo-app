from fastapi import FastAPI
from app.routes.tasks import router as task_router



app=FastAPI()


@app.get("/")
def home():
    return {"message":"Hello, To-Do app  By Jassim!"}

app.include_router(task_router)