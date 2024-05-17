from pymongo import MongoClient

hostname = 'localhost'
portnumber = 27017


#conn_obj = MongoClient('mongodb://localhost:27017') 
conn_obj = MongoClient(hostname, portnumber)
print(conn_obj)

