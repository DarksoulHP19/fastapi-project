from fastapi import FastAPI
from models import Todo

app = FastAPI()

@app.get("/")
async def read_root():
    return {"MESSAGE": "Hello World"}





''''
#advantages of FastAPI

1. it's just python and same as a flask and django
2. it's faster than flask and django
3. async is built in.
4. built in data validation using pydantic.
5. it's typed python.
6. error in json
7. support for websockets and HTTTP basic 0auth2 tokens {JWT token} and header api keys.
8. swagger UI and redoc for documentation.
'''

todos = []

#get all todos
@app.get("/todos")
async def get_todos():
    return {"todos": todos}



#get single todo
@app.get("/todos/{todo_id}")
async def get_todo():
    for todo in todos:
        if todo.id == todo_id:
            return {"todo": todo}
    return {"message": "TODO NOT FOUND"}


#create a todo
@app.post("/todos")
async def cretae_todos(todo: Todo):
    todos.append(todo)
    return {"MESSAGE": "TODO HAS BEEN CREATED"}

#update a todo
@app.put("/todos/{todo_id}")
async def update_todo(todo_id : int,todo_obj: Todo):
    for todo in todos:
        if todo.id == todo_id:
            todo.id = todo_id
            todo.item = todo_obj.item
            return {"todo": todo}
    return {"message": " No TODOs FOUND"}


#delete a todo
@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id : int):
    for todo in todos:
        if todo.id == todo_id:
            todos.remove(todo)
            return {"MESSAGE": "TODO HAS BEEN DELETED"}
    return {"message": "TODO NOT FOUND"}