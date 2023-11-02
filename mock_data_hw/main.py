import csv
import pandas as pd
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/mock_data/")
def read_mock_data():
    # Read the CSV file
    with open('mock_data.csv', mode='r', newline='') as file:
        reader = csv.reader(file)
        rows = [row for row in reader]

    # Select 1000 rows
    selected_rows = rows[:1000]

    return selected_rows