from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def user() -> dict:
    return {"name" : "faridun",
            "age": 19}

@app.get("/contacts")
def contacts() -> int:
    return 902991188

post = [
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

@app.get("/posts")
async def posts() -> list:
    return post
