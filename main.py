from fastapi import FastAPI


app = FastAPI()

@app.get("/hello")
async def hello_word():
    return {"message" : "Hello world"}
