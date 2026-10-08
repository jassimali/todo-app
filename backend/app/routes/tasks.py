from fastapi import APIRouter

from app.schemas.task import TaskCreate, TaskUpdate, TaskPatch


router = APIRouter()

tasks = []


@router.get("/tasks")
def get_tasks():
    return tasks


@router.post("/tasks")
def create_task(task: TaskCreate):
    new_task = {
        "id": len(tasks) + 1,
        "title": task.title,
        "completed": False
    }

    tasks.append(new_task)

    return new_task


@router.put("/tasks/{task_id}")
def update_task(task_id: int, task: TaskUpdate):

    for existing_task in tasks:

        if existing_task["id"] == task_id:
            existing_task["title"] = task.title
            existing_task["completed"] = task.completed

            return existing_task

    return {"message": "Task not found"}


@router.patch("/tasks/{task_id}")
def patch_task(task_id: int, task: TaskPatch):

    for existing_task in tasks:

        if existing_task["id"] == task_id:

            if task.title is not None:
                existing_task["title"] = task.title

            if task.completed is not None:
                existing_task["completed"] = task.completed

            return existing_task

    return {"message": "Task not found"}


@router.delete("/tasks/{task_id}")
def delete_task(task_id: int):

    for existing_task in tasks:

        if existing_task["id"] == task_id:
            tasks.remove(existing_task)

            return {"message": "Task deleted"}

    return {"message": "Task not found"}