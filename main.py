from fastapi import FastAPI, HTTPException, Path
from typing import Optional,List, Dict, Annotated
from pydantic import BaseModel

app = FastAPI()



@app.get("/")
def user() -> dict:
    return {"name" : "faridun",
            "age": 19}

@app.get("/contacts")
def contacts() -> int:
    return 902991188

class Author(BaseModel):
    id: int
    name: str
    age: int

class Post(BaseModel):
    id:int
    title:str
    text:str
    author: Author

class PostCrate(BaseModel):
    title: str
    body: str
    author_id : int


authors =[
    {
     'id': 1,
     'name' : 'Qurbon',
     'age':18
    },

    {
     'id': 2,
     'name' : 'Alex',
     'age':30
     },
    {
     'id': 3,
     'name' : 'Bob',
     'age':23
     }
]

posts = [
    {
     'id' : 1,
     'title' : 'Name 1',
     'text' : 'Text 1',
     'author' :  authors[1]
     },
    {
     'id' : 2,
     'title' : 'Name 2',
     'text' : 'Text 2',
     'author' :  authors[1]
    },
    {
     'id' : 3,
     'title' : 'Name 3',
     'text' : 'Text 3',
     'author' :  authors[1]
    }
]

@app.get("/items")
async def items() -> List[Post]:
    return [Post(**post) for post in posts]

@app.post("/item/add")
async def add_item(post: PostCrate) -> Post:
    post_author = next((author for author in authors if authors['id'] == post.author_id), None)
    if not post_author:
        raise HTTPException(status_code=404, detail="Author not found")

    new_post_id = len(posts) + 1

    new_post = {'id':new_post_id, 'title':post.title, 'body':post.body, 'author': post_author}
    posts.append(new_post)
    return Post(**new_post)

@app.get("/items/{id}")
async def items(id: Annotated[int, Path(..., title = ' Здесь указывается id поста')], ge=1, lt=100 ) -> Post:
    for post in posts:
        if post['id'] == id :
            return Post(**post)

    raise HTTPException(status_code=404, detail="Post not found")

@app.get("/search")
async def search(post_id: Optional[int] = None) -> Dict[str, Optional[Post]]:
    if post_id is not None:
        for post in posts:
            if post["id"] == post_id:
                return {'data': Post(**post)}
        raise HTTPException(status_code=404, detail="Post not found")
    else:
        return {"data": None}
