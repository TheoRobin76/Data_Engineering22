import pymongo
client = pymongo.MongoClient("mongodb://3.68.214.183")
db = client['sparta']

myles = db.trainees.find_one({"name": "Myles"})
print(myles)

matt = db.trainees.find_one({"name": "Matt"})
print(matt)

