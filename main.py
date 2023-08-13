import uvicorn
from fastapi import FastAPI
import numpy as np
import pandas as pd

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/response/")
async def read_root():
    return {"response": "success3"}

@app.get("/count/")
async def read_root(input_string: str, number: int):
    result = len(input_string)
    return {"letters": result, "number": number}
    #return {result,"letters:"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)


