## TASK 3 -- how to use on WSL ubuntu
## in order to run this task go to wsl terminal and place where the code is held
## run commend "uvicorn main:app --reload"
## this will set the server and under "http://127.0.0.1:8000/mock_data/"
## you can find the selected rows!:)
## tutorial: https://fastapi.tiangolo.com/tutorial/first-steps/

import csv
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/mock_data/")
def read_mock_data():
    # Read the CSV file
    with open('user_records_large.csv', mode='r', newline='') as file:
        reader = csv.reader(file)
        rows = [row for row in reader]

    # Select 1000 rows
    selected_rows = rows[:1000]

    return selected_rows

