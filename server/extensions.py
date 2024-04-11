from flask_pymongo import PyMongo
from pymongo import MongoClient
from dotenv import load_dotenv
import os


# Load ENV
load_dotenv()

# Setup MongoDB here
uri = os.getenv("MONGODB_URI")
# mongo = PyMongo(uri="mongodb://localhost:27017/database")

# Create a new client and connect to the server
client = MongoClient(uri)
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)