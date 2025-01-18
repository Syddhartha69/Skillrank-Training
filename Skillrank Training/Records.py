from pymongo import MongoClient
from faker import Faker
import random
import time

# Step 1: Connect to MongoDB Atlas
connection_string = "mongodb+srv://<username>:<password>@databasename.0c6c8.mongodb.net/"  
client = MongoClient(connection_string)
db = client["sample_database"]  
collection = db["sample_collection"]

# Step 2: Generate Fake Data
fake = Faker()

def generate_record():
    """Generate a single record."""
    return {
        "name": fake.name(),
        "email": fake.email(),
        "address": fake.address(),
        "phone_number": fake.phone_number(),
        "age": random.randint(18, 80),
        "signup_date": fake.date_time_this_decade(),
        "active": random.choice([True, False])
    }

# Step 3: Bulk Insert 100,000 Records
def insert_bulk_records(record_count=100000, batch_size=1000):
    """Insert records in bulk."""
    total_inserted = 0
    start_time = time.time()
    for _ in range(record_count // batch_size):
        batch = [generate_record() for _ in range(batch_size)]
        collection.insert_many(batch)
        total_inserted += batch_size
        print(f"Inserted {total_inserted}/{record_count} records...")

    # Handle any remainder if record_count is not a multiple of batch_size 
    remainder = record_count % batch_size
    if remainder > 0:
        batch = [generate_record() for _ in range(remainder)]
        collection.insert_many(batch)
        total_inserted += remainder
        print(f"Inserted {total_inserted}/{record_count} records...")

    end_time = time.time()
    print(f"Completed inserting {total_inserted} records in {end_time - start_time:.2f} seconds.")

# Run the bulk insert function
insert_bulk_records()
