import pymongo
connectionString = "mongodb+srv://Siddhartha:Sid123@cluster0.hptv1.mongodb.net/"

if __name__ == "__main__":
    client = pymongo.MongoClient(connectionString)
    # creating a database for school XYZ
    db = client["XYZ-School"]

    # creating a collection 
    collection = db.class1

    # inserting into a document 
    studentInfo = {
        "name" : "sid",
        "Section" : 1, 
        "maths_marks" : 100,
        "Science_Marks" : 79,
    }
    student_id = collection.insert_one(studentInfo).inserted_id
    print(student_id, "Has been created") 