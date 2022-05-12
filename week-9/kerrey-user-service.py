# ============================================
# Title: Exercise 9.2 - Querying and Creating Documents
# File Name: kerrey_user-service.py
# Author: Professor Krasso
# Date: 15 May 2022
# Modified By: Seth Kerrey
# Description:
#   Learn how to query and create documents 
#   in a MongoDB database instance through Python and pymongo.
# Resources:
#   buwebdev, Professor Krasso, Bellevue University
# ===========================================

# import statements
from pymongo import MongoClient
import pprint
import datetime

# connect to MongoDB instance
client = MongoClient("localhost", 27017) 
db = client.web335

# create user document 
user = {
  "first_name": "James",
  "last_name": "Bond",
  "email": "agent007@mail.com",
  "employee_id": "007",
  "date_created": datetime.datetime.utcnow()
}

#import user document
user_id = db.users.insert_one(user).inserted_id

print(user_id)
pprint.pprint(db.users.find_one({"employee_id": "007"}))