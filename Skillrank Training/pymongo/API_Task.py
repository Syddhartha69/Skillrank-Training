from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection
connection_string = "mongodb+srv://<Username>:<password@<databasename>.12345.mongodb.net/"
client = MongoClient(connection_string)

# Database and collection
db = client["sample_database"]  # database name
collection = db["sample_collection"]  # collection name

# Endpoint to list all data
@app.route('/api/data', methods=['GET'])
def get_all_data():
    try:
        # Fetch all documents from the collection
        data = list(collection.find({}, {"_id": 0}))  # Exclude the '_id' field
        return jsonify(data), 200  # Return the data as JSON with status code 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Handle errors gracefully

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
