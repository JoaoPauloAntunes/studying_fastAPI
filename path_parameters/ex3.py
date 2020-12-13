from fastapi import FastAPI

app = FastAPI()

# este caminho deve ser declado antes do /users/{user_id}
@app.get("/users/me")
def read_user_me():
    return {"user_id": "the current user"}

@app.get("/users/{user_id}")
def read_user(user_id: str):
    return {"user_id": user_id}