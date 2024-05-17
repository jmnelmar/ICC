from pymongo import MongoClient
conn_obj = MongoClient('mongodb://localhost:27017/')
database_obj = conn_obj['ETA']
collection_obj = database_obj['student']
print('Before Dropping the collection:')
for doc in collection_obj.find():
    print(doc)
#Dropping the collection
collection_obj.drop()
print('After Dropping the collection:')
for doc in collection_obj.find():
    print(doc)
