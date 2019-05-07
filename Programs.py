# >>>>>>>>>>>>>>>>>Exception handling<<<<<<<<<<<<<<<<<<<

def divide(num):
    result = 100/num
    print('Division by zero not allowed')
    print('Result is: ', result)
divide(0)

# ------------------------------------------

def divide(num):
    try:
        result = 100/num
    except ZeroDivisionError:
        print('Division by zero not allowed')
    else:
        print('Result is: ', result)

if __name__ == "__main__":
    divide(0)

# ------------------------------------------
def convert(val):
    val = int(val)
    print('Passed value: ', val)
   
convert('d')


# ------------------------------------------
def convert(val):
    try:
        val = int(val)
        print('Passed value: ', val)
    except ValueError:
        print('val type is not int')
convert('d')

# ------------------------------------------
# writing a file
with open("test.txt",'w',encoding = 'utf-8') as f:
   f.write("my first file\n")
   f.write("This file\n")
   f.write("contains three lines\n")

f = open('test.txt')
print(f.read())

# ------------------------------------------
# read a file
f = open("test.txt",'r',encoding = 'utf-8')

print(f.read(5)) # read the first 5 data

print(f.tell())    # get the current file position

print(f.seek(2))   # bring file cursor to initial position

print(f.read())  # read the entire file

print(f.readline()) # read individual lines of a file till the newline encounter

print(f.readlines()) # read individual lines of a file

# MongoDB Insert-------------

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


# MongoDB Find-------------

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["mycollections"]

x = mycol.find_one()   # returns  first occurrence in the selection
print(x)

for x in mycol.find(): # returns all the documents in collections
  print(x)

# MongoDB Update-------------
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["mycollections"]

myquery = { "address": "Highway 7" }
newvalues = { "$set": { "address": "Canyon 123" } }

mycol.update_one(myquery, newvalues) # Updates one record

mycol.update_many(myquery, newvalues) # Updates many records which matches search criteria 

#print "mycollections" after the update:
for x in mycol.find():
  print(x)

# MongoDB Delete-------------
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
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
