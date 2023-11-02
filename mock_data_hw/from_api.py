import os
import csv
import dotenv
import requests
import itertools


n_api_requests = 1000
api_end_point = "mock_data"
dotenv.load_dotenv()

data = list(itertools.chain.from_iterable(
    requests.get(os.getenv(api_end_point)).csv() 
    for _ in range(n_api_requests)
))

with open('api_request_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

