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

@app.post("/tasks")
def create_tasks():
    return {"message":"This is your new created tasks"}

@app.put("/tasks")
def update_tasks():
    return {"message":"This is the updated task"}

@app.get("/hello")
def print_hello():
    return {"message":"from hello huuhuhhhhuh 🙂"}