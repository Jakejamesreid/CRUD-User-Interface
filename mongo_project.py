import pymongo
import os
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
if os.path.exists(__location__+"\\env.py"):
    import env

MONGODB_URI = os.environ.get("MONGO_URI")
DBS_NAME = os.environ.get("DBS_NAME")
COLLECTION_NAME = os.environ.get("COLLECTION_NAME")

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected!")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e

conn = mongo_connect(MONGODB_URI)
coll = conn[DBS_NAME][COLLECTION_NAME]

# Find all entries in the DB
documents = coll.find()
for doc in documents:
    print(doc)