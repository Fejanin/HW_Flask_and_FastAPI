from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates


class Task(BaseModel):
    id: int
    title: str
    description: str
    status: str

app = FastAPI()
templates = Jinja2Templates(directory='HW_5/templates')

tasks = []

@app.get('/tasks/', response_class=HTMLResponse)
async def get_tasks(request: Request):
    data = {}
    print(tasks)
    for i in range(len(tasks)):
        data[i] = {'id': tasks[i].id,
                   'title': tasks[i].title,
                   'description': tasks[i].description,
                   'status': tasks[i].status}
    return templates.TemplateResponse('tasks.html', {'request': request, 'data': data})


@app.get('/tasks/{task_id}/')
async def get_task(task_id: int):
    print(task_id)
    for i in tasks:
        if i.id == task_id:
            return i
    raise HTTPException(status_code=404, detail='Task not found.')


@app.post('/tasks/')
async def add_task(task: Task):
    task.id = len(tasks)
    task.title = f'Task №{task.id}.'
    task.description = f'It`s the {task.id} description.'
    task.status = 'active'
    tasks.append(task)
    return {'message': f'Task №{task.id} was added.'}


@app.put('/tasks/{task_id}/')
async def update_task(task_id: int):
    for i in range(len(tasks)):
        if tasks[i].id == task_id:
            if tasks[i].status == 'active':
                tasks[i].status = 'not active'
            else:
                tasks[i].status = 'active'
            return {'message': f'Status task №{task_id} was changed.'}
    raise HTTPException(status_code=404, detail='Task not found.')


@app.delete('/tasks/{task_id}/')
async def delete_task(task_id: int):
    for i, task in enumerate(tasks):
        if task.id == task_id:
            del tasks[i]
            return {'message': 'Task was deleted.'}
    raise HTTPException(status_code=404, detail='Task not found.')
