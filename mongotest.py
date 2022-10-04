import pymongo
client = pymongo.MongoClient("mongodb+srv://mitankshi143:mita143@cluster0.9o9eeyi.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name": "sudhanshu",
    "email_id": "sudhanshu@ineuron.ai",
    "surname": "kumar"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)

