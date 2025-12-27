from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def user() -> dict:
    return {"name" : "faridun",
            "age": 19}