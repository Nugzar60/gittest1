import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/response/")
async def read_root():
    a = 1
    b = 4
    return {"response": "success3"}

@app.get("/count/")
async def read_root():
# Определяем переменную str
    str = "Hello, World!"

# Выполняем операцию с переменной str
    result = len(str)

# Выводим результат на экран
    print("letters:",result)
    print("privet papa")
    return {result,"letters:"}

#    return {"str": "Hello world!"}
#   return {"letters": 11}
#    my_string: str ='Hello, world!'
#    print(len(my_string))





if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

















# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(name)  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    import numpy as np
    import pandas as pd


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import numpy as np
import pandas as pd

