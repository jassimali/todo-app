from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()




tasks=[{"id":1,"title":"Learn Python","completed":False},
       {"id":2,"title":"Built To Do App","completed":False}]


class TaskCreate(BaseModel):       #creating a blueprint of data coming ,, to define the shape of data our API expects
    title: str

class TaskUpdate(BaseModel):                    #last
    title: str
    completed: bool

class TaskPatch(BaseModel):
    title: str | None = None
    completed: bool | None = None


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



@app.put("/tasks/{task_id}")
def update_tasks(task_id: int,task :TaskUpdate):
    for existing_task in tasks:
        if existing_task["id"]==task_id:
            existing_task["title"]=task.title
            existing_task["completed"]=task.completed
            return existing_task
    return {"message":"Task not found"}


@app.delete("/tasks/{task_id}")
def delete_tasks(task_id : int):
    for existing_task in tasks:
        if existing_task["id"]==task_id:
            tasks.remove(existing_task)

            for t in tasks:                             #to reindex remaining items
                if t["id"] > task_id:
                    t["id"] -= 1

            return {"message":f"Deleted the task ${existing_task["title"]} Successfully"}
    return {"message":"Task not found"}


@app.patch("/tasks/{task_id}")
def patch_tasks(task_id :int,task :TaskPatch):
    for existing_task in tasks:
        if existing_task["id"]==task_id:
            if task.title is not None:
                existing_task["title"] = task.title

            if task.completed is not None:
                existing_task["completed"] = task.completed
            return existing_task
    return {"message":"Task not found"}


@app.get("/hello")
def print_hello():
    return {"message":"from hello huuhuhhhhuh 🙂"}