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
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e

def show_menu():
    print()
    print("Option 1. Create")
    print("Option 2. Find")
    print("Option 3. Update")
    print("Option 4. Delete")
    print("Option 5. Exit")
    print("")

    option = input("Enter an option:")
    return option

def add_record():
    fname = input("Enter first name: ")
    lname = input("Enter last name: ")
    dob = input("Enter date of birth: ")
    gender = input("Enter gender: ")
    hair_colour = input("Enter hair colour: ")
    occupation = input("Enter occupation: ")
    nationality = input("Enter nationality: ")

    try:
        coll.insert({"first": fname.lower(), "last": lname.lower(), "dob": dob, "gender": gender, "hair_colour": hair_colour, "occupation": occupation, "nationality": nationality})
        print()
        print("Document Inserted")
    except:
        print("Error accessing the database")

def main_loop():
    while True:
        option = show_menu()
        if option == "1":
            print("You have selected option 1")
            add_record()
        elif option == "2":
            print("You have selected option 2")
        elif option == "3":
            print("You have selected option 3")
        elif option == "4":
            print("You have selected option 4")
        elif option == "5":
            conn.close()
            break
        else:
            print("Invalid option")
        print("")

conn = mongo_connect(MONGODB_URI)
coll = conn[DBS_NAME][COLLECTION_NAME]

main_loop()