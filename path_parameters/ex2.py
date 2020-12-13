from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: int): # using stardard Python type annotation
    return {"item_id": item_id}