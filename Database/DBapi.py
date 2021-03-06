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
            query["plotName"] = {"$regex" : plotName}
        if author:
            query["author"] = {"$regex" : author}
        if actor:
            query["characters.actor"] = {"$regex" : actor}

        if Basic.count_documents(query) == 0:
            print("can not find this document")
            return False

        return Basic.find(query)
    except pymongo.errors.PyMongoError as e:
        return False

def deleteDocs(objID):
    try:
        Basic = db["Basic"]
        Content = db["Content"]
        queryBasic = {"_id" : objID}
        queryContent = {"BasicID" : objID}

        Basic.delete_one(queryBasic)
        Content.delete_one(queryContent)

        return True
       
    except pymongo.errors.PyMongoError as e:
        return False

def findContent(objID):
    try:
        Content = db["Content"]
        query = {"BasicID" : objID}

        return Content.find_one(query)
        
    except pymongo.errors.PyMongoError as e:
        return False

# Tab2 api
def upsertBasic(data , objID = None):
    Basic = db["Basic"]
    Content = db["Content"] 
    
    name = list()

    for i in data["characters"]:
        name.append(i["name"])
    
    #update
    if objID:
        try:
            Basic.update_one({"_id" : objID} , {"$set" : {
                                                        "plotName" : data["plotName"] , 
                                                        "author" : data["author"] , 
                                                        "outline" : data["outline"] , 
                                                        "type" : data["type"],
                                                        "photo" : data["photo"],
                                                        "characters" : data["characters"],
                                                        }
                                                }
            )
        
            Content.update_one({"BasicID" : objID} , {"$set" : {"plotName" : data["plotName"] , "characters" : name}})

            return True
        except pymongo.errors.PyMongoError as e:
            return False
    # insert
    else:     
        try:
            BasicID = Basic.insert_one(data).inserted_id
            Content.insert_one({"BasicID" : BasicID , "plotName" : data["plotName"] , "characters" : name , "scene" : None})
            return True
        except pymongo.errors.PyMongoError as e:
            return False   

# Tab3 api
def updateContent(BasicID , scene):
    Content = db["Content"]
    query = {"BasicID" : BasicID}

    try:
        Content.update_one(query , {"$set" : {"scene" : scene}})
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

# delete all documents
def deleteMongodb():
    db["Basic"].delete_many({})
    db["Content"].delete_many({})
    db["fs.chunks"].delete_many({})
    db["fs.files"].delete_many({})

# connectDB()
# deleteMongodb()

