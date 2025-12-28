from fastapi import FastAPI, HTTPException
from typing import Optional

app = FastAPI()

@app.get("/")
def user() -> dict:
    return {"name" : "faridun",
            "age": 19}

@app.get("/contacts")
def contacts() -> int:
    return 902991188

posts = [
    {"id" : 1,
     "title" : "Name 1",
     "text" : "Text 1"
     },
    {
     "id" : 2,
     "title" : "Name 2",
     "text" : "Text 2"
    },
    {
     "id" : 3,
     "title" : "Name 3",
     "text" : "Text 3"
    }
]

@app.get("/items")
async def items() -> list:
    return posts

@app.get("/items/{id}")
async def items(id: int) -> dict:
    for post in posts:
        if post['id'] == id :
            return post

    raise HTTPException(status_code=404, detail="Post not found")

@app.get("/search")
async def search(post_id: Optional[int] = None) -> dict:
    if post_id is not None:
        for post in posts:
            if post["id"] == post_id:
                return post
        raise HTTPException(status_code=404, detail="Post not found")
    return {"data": "No post id provided"}
