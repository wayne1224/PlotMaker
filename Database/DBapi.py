import pymongo
import datetime
import time
import calendar
import gridfs
import os
from bson.objectid import ObjectId

# connect to datebase
def connectDB():
    global db
    global Basic
    global Content
    client = pymongo.MongoClient()
  
    try:
        # host = os.environ.get('URI')
        # print(host)
        host = "mongodb+srv://wayne1224:wayne1224@sandbox.qjd2q.mongodb.net/myFirstDatabase?authSource=admin&replicaSet=atlas-bu8995-shard-0&w=majority&readPreference=primary&appname=MongoDB%20Compass&retryWrites=true&ssl=true"
        client = pymongo.MongoClient(host , serverSelectionTimeoutMS = 10000) # Timeout 10s    
        db = client["PlotMaker"] # choose database
        Basic = db["Basic"] # choose collection
        Content = db["Content"] # choose collection

        client.server_info()
        return True

    except Exception as e:
        print(e)
        client.close()
        return False

def upsertBasic(objID , Basic): 
    if objID:
        pass

def insertImg(path):
    grid = gridfs.GridFS(db)
    file = open(path , 'rb')
    objId = grid.put(file)
    file.close()

    return objId
   
def findImg(objID):   
    grid = gridfs.GridFS(db)

    if grid.exists({"_id" : objID}):
        return grid.find_one({"_id" : objID}).read()
        # return grid.get_last_version(filename = None , _id = objID).read()

objID = ObjectId("60a8cd2855497c05787dbe12")
path = 'C:\\Users\\HAO\\Desktop\\Pic\\image0.jpg'

connectDB()
# print(insertImg(path))
# print(findImg(objID))

