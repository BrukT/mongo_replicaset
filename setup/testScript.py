from pymongo import MongoClient

uri = "mongodb://bruk:bruk@mongo1:27017,mongo2:27017,mongo3:27017/?replicaSet=rs0&authSource=admin"
uri = "mongodb://bruk:bruk@mongo1:27017/?replicaSet=rs0&authSource=admin"
client = MongoClient(uri,connect=False)
print(client)
#client = MongoClient('mongo1:27011', username='bruk', password='bruk', authSource='admin', replicaSet='rs0')
#db = client['admin']
#db.authenticate('bruk','bruk')

for l in client.list_databases():
    print(l)
print("list of collections")
db = client.get_database("test");
for l in db.list_collections():
    print(l)

db.get_collection("user")
coll = db.get_collection("user")
print("Inside one collection")

coll.insert_one({'name' : 'tena'})
print(coll.find_one())