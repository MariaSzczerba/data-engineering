from faker import Faker
import random
import csv

fake = Faker()

# Set a seed for reproducibility
random.seed(42)

# Generate Users Dataset
def generate_users(num_records):
    users = {}
    for id in range(num_records):
        users[id] = fake.name()
    return users

# Generate Users Information Dataset
def generate_users_info(users):
    user_info = [['id', 'user_name', 'email', 'date_of_birth']]
    user_location = [['id', 'user_name', 'address']]
    accounts = [['id', 'user_name', 'account_number']]
    emergancy_contact = [['id', 'contact_name', 'contact_phone_number']]
    for id, user_name in users.items():
        user_info.append([id, user_name, fake.email(), fake.date_of_birth()])
        user_location.append([id, user_name, fake.address()])
        accounts.append([id, user_name, fake.uuid4()])
        emergancy_contact.append([id, fake.name(), fake.phone_number()])
    return user_info, user_location, accounts, emergancy_contact

# Generate Transactions Dataset
def generate_transactions(num_records, num_users, users):
    transactions = [['transaction_id', 'id', 'user_name', 'amount', 'date_of_transaction']]
    for _ in range(num_records):
        random_id_user = random.randint(0, num_users - 1)
        transactions.append([fake.uuid4(), random_id_user, users[random_id_user], random.uniform(1, 10000), fake.date_time_this_year()])
    return transactions

# Set the number of records for each dataset
num_users = 10000
num_records = 100000

# Generate and write datasets to CSV files
users = generate_users(num_users)
user_info, user_location, accounts, emergancy_contact = generate_users_info(users)
transactions_data = generate_transactions(num_records, num_users, users)

# Write to CSV
def write_to_csv(data, filename):
    with open(filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerows(data)

write_to_csv(user_info, 'data/user_info.csv')
write_to_csv(user_location, 'data/user_location.csv')
write_to_csv(accounts, 'data/accounts.csv')
write_to_csv(emergancy_contact, 'data/emergancy_contact.csv')
write_to_csv(transactions_data, 'data/transactions.csv')
