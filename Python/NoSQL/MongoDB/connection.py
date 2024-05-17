from typing import Any
from pymongo import MongoClient



class MongoConnection:

    def __init__(self, hostname, portnumber):
        self._hostname = hostname
        self._portnumber = portnumber
        self._status = "inactive"
        self._conn_obj = None
        self._database_obj = None
        self._collection_obj = None

    def get_collection(self):
        return self._collection_obj
    
    def get_database(self):
        return self._database_obj

    def open(self):
        try:
            #conn_obj = MongoClient('mongodb://localhost:27017') 
            self._conn_obj = MongoClient(self._hostname, self._portnumber)
            self._status = self._conn_obj.server_info()
        except pymongo.errors.ConnectionFailure:
            print(f"Failed to connect to the server {self._hostname}:{self._portnumber}")

    def get_status(self):
        self._conn_obj.list_database_names()
    
    def close(self):
        self._conn_obj.close()

    def use_database(self, databasename):
        databases = self.fetch_databases()
        if databasename not in databases:
            print(f"Database {databasename} is not found, proceding to create database 📦")
        else:
            print("Databes found, switching to the database 🔌")
        self._database_obj = self._conn_obj[databasename] 

    def use_collection(self, collectionname):
        collections = self.fetch_collections()
        if collectionname not in collections:
            print(f"Collection {collectionname} does not exists, creating the collection 🖥️")
        else:
            print(f"Accesising to the collection {collectionname} 📥")
        self._collection_obj = self._database_obj[collectionname]

    def fetch_databases(self):
        return self._conn_obj.list_database_names()
    
    def fetch_collections(self):
        return self._database_obj.list_collection_names()

    def insert(self, document):
        obj = self._collection_obj.insert_one(document)
        return obj.inserted_id
    
    def insert_many(self, documents):
        obj = self._collection_obj.insert_many(documents)
        return obj
    
    def search(self,filter = None):
        docs = None
        if filter is None:
            docs = self._collection_obj.find()
        else:
            docs = self._collection_obj.find(filter)
        return docs
    
    def get_first_collection(self):
        doc = self._collection_obj.find_one()
        return doc


def print_students(docs, filter = None):
    str = "Getting all the documents"
    if filter is not None:
        str += f" with the filter: {filter}"
    print(str)
    print(f"Name\tAge\tSex")
    for doc in docs:
        print(f"{doc['Name']}\t{doc['Age']}\t{doc['Sex']}")

mongoconnection = MongoConnection("localhost",27017)
mongoconnection.open()
print(mongoconnection.fetch_databases())
mongoconnection.use_database("ETA")
print(mongoconnection.fetch_collections())
mongoconnection.use_collection("student")
docs = mongoconnection.search()
print("fetching all the documents in student")
print_students(docs)
filter = {'Sex':'F'}
docs = mongoconnection.search(filter)
print_students(docs,filter)

filter = {"Age":{"$gt":20}}
docs = mongoconnection.search(filter)
print_students(docs, filter)

filter = {"Age":{"$eq":20}}
docs = mongoconnection.search(filter)
print_students(docs,filter)

filter = {"Age":{"$ne":20}}
docs = mongoconnection.search(filter)
print_students(docs, filter)

filter = {"Age":{"$gte":21}}
docs = mongoconnection.search(filter)
print_students(docs, filter)

filter = {"Age":{"$lt":21}}
docs = mongoconnection.search(filter)
print_students(docs, filter)

filter = {"Age":{"$lte":19}}
docs = mongoconnection.search(filter)
print_students(docs, filter)

#filter using regex to filter all the students who start with the letter R
filter = {'Name':{'$regex':'^R'}}
docs = mongoconnection.search(filter)
print_students(docs, filter)
'''
document = {'Name':'John','Regd_id':'1','Age':20,'Sex':'M'}
id = mongoconnection.insert(document)
print(f"Document id: {id} was inserted 🤖")

document_list = [
    {'Name':'Kelley','Regd_id':'2','Age':21,'Sex':'M'},
    {'Name':'Hannah','Regd_id':'3','Age':18,'Sex':'F'},
    {'Name':'Ravi','Regd_id':'4','Age':22,'Sex':'M'},
    {'Name':'Rachel','Regd_id':'5','Age':26,'Sex':'F'},
    {'Name':'Esther','Regd_id':'6','Age':19,'Sex':'F'}
]

ids = mongoconnection.insert_many(document_list)

print(f"Objects were inserted with the ids: {ids} 🪄")
'''
mongoconnection.close()