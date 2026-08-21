from fastapi import FastAPI

app=FastAPI()

tasks=[{"id":1,"title":"Learn Python","Completed":False},
       {"id":2,"title":"Built To Do App","Completed":False}]

@app.get("/")
def home():
    return {"message":"Hello, To-Do app  By Jassim!"}

@app.get("/tasks")
def get_tasks():
    return tasks
