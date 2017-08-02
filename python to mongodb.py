import pymongo
from pymongo import MongoClient
client = MongoClient('localhost:27017')
Pythondb = client.Pythondb
Employees = Pythondb.Employees

#data inserting
myrecord ={"id":"0001","name":"Mongodb","age":"05","Dept":"IT","country":"India"}

# find data
query = Employees.find({})

query1 = Pythondb.Employees.insert(myrecord)

#print data
for doc in query:
    print(doc)

print("Inserted doc ID = ",query1)
