from pymongo import MongoClient
from dotenv import load_dotenv
import os

rec = [{
    'name': 'light aladim',
    'age': 34,
}]
load_dotenv()

url = os.getenv('MONGO_LOCAL_DB')

def get_database():
 
   # Provide the mongodb atlas url to connect python to mongodb using pymongo
   CONNECTION_STRING = str(url)
 
   # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
   client = MongoClient(CONNECTION_STRING)
 
   # Create the database for our example (we will use the same database throughout the tutorial
   return client['yearn']
  
# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":   
  
#   getting the various collections in the database
   # Get the database
   print(f"Connecting to {url}")
   dbname = get_database()
   adminDB = dbname['admin']
   userDB = dbname['user']
   adminDB.insert_one({
       'name': 'admin',
       
   })