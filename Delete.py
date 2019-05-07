import pymongo

myclient = pymongo.MongoClient("mongodb://mongo4:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["mycollections"]

myquery = { "address": "Highway 7" }

mycol.delete_one(myquery)

# x = mycol.delete_many(myquery)
# x = mycol.delete_many({}) # Deletes all data in collection

# print(x.deleted_count, " documents deleted.")

# mydoc = mycol.find().sort("name") #Sort the result alphabetically by name
# mycol.drop() # Delete the "mycollections" collection:
# myresult = mycol.find().limit(5)


for x in mycol.find():
  print(x)
