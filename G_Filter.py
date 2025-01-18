from pymongo import MongoClient

# MongoDB Atlas connection
connection_string = "mongodb+srv://<Username>:<password@<databasename>.12345.mongodb.net/"
client = MongoClient(connection_string)

# Database and collection
db = client["sample_database"]  # database name
collection = db["sample_collection"]  # collection name

# Query data with specific filter
filter_query = {
    "name": {"$regex": "^G"},  # Name starts with 'G'
    "age": {"$gte": 20, "$lte": 32},  # Age between 20 and 32
    "active": False  # Active is false
}


# File to store names
output_file = "filtered_names.txt"

# Fetch and write names to a file
with open(output_file, "w") as file:
    results = collection.find(filter_query)
    for record in results:
        name = record.get("name", "Unknown")
        age = record.get("age", "Unknown")
        file.write(f"Name: {name}, Age: {age}\n")
        print(f"Written to file: Name: {name}, Age: {age}")

print(f"Names starting with 'G' have been written to {output_file}.")