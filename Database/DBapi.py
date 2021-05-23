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
    client = pymongo.MongoClient()
  
    try:
        # host = os.environ.get('URI')
        # print(host)
        host = "mongodb+srv://wayne1224:wayne1224@sandbox.qjd2q.mongodb.net/myFirstDatabase?authSource=admin&replicaSet=atlas-bu8995-shard-0&w=majority&readPreference=primary&appname=MongoDB%20Compass&retryWrites=true&ssl=true"
        client = pymongo.MongoClient(host , serverSelectionTimeoutMS = 10000) # Timeout 10s    
        db = client["PlotMaker"] # choose database

        client.server_info()
        return True

    except Exception as e:
        print(e)
        client.close()
        return False


# Tab1 api
def findDocs(plotName , author , actor):
    try:
        Basic = db["Basic"]
        query = dict()

        if plotName:
            query["plotName"] = plotName
        if author:
            query["author"] = author
        if actor:
            query["characters.actor"] = actor

        if Basic.count_documents(query) == 0:
            print("can not find this document")
            return False

        return Basic.find(query)
    except pymongo.errors.PyMongoError as e:
        return False

# Basic api
def upsertBasic(objID , data): 
    Basic = db["Basic"] # choose collection
    result = ["" , ""]

    #update
    if objID:
        result[0] = "update" 
        try:
            Basic.update_one({"_id" : objID} , {"$set" : {
                                                        "plotName" : data["plotName"] , 
                                                        "author" : data["author"] , 
                                                        "outline" : data["outline"] , 
                                                        "type" : data["type"],
                                                        "charaters" : data["charaters"]
                                                        }
                                                }
            )
            result[1] = True
        except pymongo.errors.PyMongoError as e:
            result[1] = False
    # insert
    else:
        Content = db["Content"]
        result[0] = "insert"
        
        try:
            BasicID = Basic.insert_one(data).inserted_id
            Content.insert_one({"BasicID" : BasicID , "plotName" : data["plotName"] , "content" : None})
            result[1] = True
        except pymongo.errors.PyMongoError as e:
            result[1] = False    

    return result

# Content api
def updateContent(BasicID , plotName , content):
    Content = db["Content"]
    query = {"BasicID" : BasicID , "plotName" : plotName}

    try:
        Content.update_one(query , {"$set" : {"Content" : content}})
        return True
    except pymongo.errors.PyMongoError as e:
        return False
    
# Image api
def insertImg(path):
    grid = gridfs.GridFS(db)
    file = open(path , 'rb')
    objID = grid.put(file)
    file.close()

    return objID
   
def findImg(objID):   
    try:
        grid = gridfs.GridFS(db)

        if grid.exists({"_id" : objID}):
            return grid.find_one({"_id" : objID}).read()
    except pymongo.errors.PyMongoError as e:
        return False

objID = ObjectId("60a8cd2855497c05787dbe12")
path = 'C:\\Users\\HAO\\Desktop\\Pic\\image0.jpg'

data = {
    "plotName" : "plotName",
    "author" : "author",
    "characters" : [{"name" : "戲名1" , "actor" : "本名1" , "objID" : "001"} ,{"name" : "戲名2" , "actor" : "本名2" , "objID" : "002"}],
    "type" : " type",
    "outline" : "outline"
}

connectDB()

# for i in findDocs("" , "" , "本名1"):
#     print(i)

# print(upsertBasic("" , data))

# print(insertImg(path))
# print(findImg(objID))

