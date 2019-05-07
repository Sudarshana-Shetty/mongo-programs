import pymongo

myclient = pymongo.MongoClient("mongodb://mongo4:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["mycollections"]

myquery = { "address": "Highway 7" }
newvalues = { "$set": { "address": "Canyon 123" } }

mycol.update_one(myquery, newvalues) # Updates one record

mycol.update_many(myquery, newvalues) # Updates many records which matches search criteria 

#print "mycollections" after the update:
for x in mycol.find():
  print(x)

