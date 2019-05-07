import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["mycollections"]
mydict = { "name": "John", "address": "Highway 7" }

mydictmultiple = [{ "name": "John", "address": "Highway 7" },
{ "name": "John2", "address": "Highway 8" }]

x = mycol.insert_one(mydict) # Inserting one record into 'mycol' collection 
print('Inserted ID: ', x.inserted_id)

x = mycol.insert_many(mydictmultiple) # Inserting many record into 'mycol' collection 

if x.acknowledged:  # return true if ewcord inserted successfully else false
    print('Record is inserted sucessfully')
else:
    print('Record insertion failed')

collections = mycol.find({})
for i in collections:
    print(i)