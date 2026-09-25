from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()




tasks=[{"id":1,"title":"Learn Python","Completed":False},
       {"id":2,"title":"Built To Do App","Completed":False}]


class TaskCreate(BaseModel):       #creating a blueprint of data coming ,, to define the shape of data our API expects
    title: str

class TaskUpdate(BaseModel):                    #last
    title: str
    completed: bool


@app.get("/")
def home():
    return {"message":"Hello, To-Do app  By Jassim!"}

@app.get("/tasks")
def get_tasks():
    return tasks

@app.post("/tasks")
def create_tasks(task: TaskCreate):
    new_task={
        "id":len(tasks)+1,
        "title":task.title,
        "completed":False
    }
    tasks.append(new_task)
    return new_task

@app.put("/tasks")
def update_tasks():
    return {"message":"This is the updated task"}

@app.get("/hello")
def print_hello():
    return {"message":"from hello huuhuhhhhuh 🙂"}