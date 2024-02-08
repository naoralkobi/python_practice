import pymongo
import time

# Connect to MongoDB
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

# Create or access the database
mydb = myclient["mydatabase"]

# Check if the database exists
dblist = myclient.list_database_names()
if "mydatabase" in dblist:
    print("Waiting for the database to be ready...")
    time.sleep(1)
    print("The database exists.")

# Create a collection (similar to a table in relational databases)
mycollection = mydb["mycollection"]

# Insert a document (similar to a row in relational databases) into the collection
mydocument = {"name": "Alex", "age": 28, "city": "Tal Aviv"}
result = mycollection.insert_one(mydocument)
print(f"Inserted document with ID: {result.inserted_id}")

# Find and print all documents in the collection
for document in mycollection.find():
    print(document)

# Update a document in the collection
query = {"name": "John Doe"}
new_values = {"$set": {"age": 31}}
mycollection.update_one(query, new_values)
print("Document updated.")

# Find and print the updated document
updated_document = mycollection.find_one(query)
print("Updated Document:")
print(updated_document)


# # Delete a document from the collection
# delete_query = {"name": "John Doe"}
# mycollection.delete_one(delete_query)
# print("Document deleted.")

# Find and print all remaining documents in the collection
remaining_documents = mycollection.find()
print("Remaining Documents:")
for document in remaining_documents:
    print(document)
