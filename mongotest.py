from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://anu:tiger@cluster0.57jxgvp.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)

db = client.test
print(db)

d = {
    "name": "Anu",
    "email": "anu@gmail.com",
    "surname": "Sasidharan"
}
d = {
    "name": "Kannan",
    "email": "kannan@gmail.com",
    "surname": "Ampady"
}
d = {
    "name": "Anu",
    "email": "anu@gmail.com",
    "surname": "Sasidharan"
}
d = {
    "name": "Kannan",
    "email": "kannan@gmail.com",
    "surname": "Ampady"
}
d = {
    "name": "Anu",
    "email": "anu@gmail.com",
    "surname": "Sasidharan"
}
d = {
    "name": "Kannan",
    "email": "kannan@gmail.com",
    "surname": "Ampady"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)