import pymongo
import datetime
import time
import calendar
import gridfs
import os

# connect to datebase
def connectDB():
    global db
    global Basic
    global Content
    client = pymongo.MongoClient()
  
    try:
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

def upsertBasic():
    pass

def insertImg(f):
    grid = gridfs.GridFS(db)
    #file = open('C:\\Users\\HAO\\Desktop\\Pic\\image0.jpg' , 'rb')
    grid.put(f , filename = "test" , content_type = "jpg")
    # file.close()

def findImg():
    grid = gridfs.GridFS(db , collection = "fs")

    for i in grid.find():
        print(i.filename)
        # print(i.read())

connectDB()
insertImg()
#findImg()

