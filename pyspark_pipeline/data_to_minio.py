import minio 

client = minio.Minio(
    "localhost:9005",
    access_key="minioadmin",
    secret_key="minioadmin",
    secure=False
)

data_set_names = ["accounts.csv", "emergency_contact.csv", "transactions.csv", "user_info.csv", "user_location.csv"]

for data_set_name in data_set_names:
    client.fput_object(
        "pyspark-task-data",
        data_set_name,
        file_path = "data/" + data_set_name
    )