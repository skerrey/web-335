# ============================================
# Title: Exercise 9.3 - Updating and Deleting Documents
# File Name: kerrey_user-update.py
# Author: Professor Krasso
# Date: 15 May 2022
# Modified By: Seth Kerrey
# Description:
#   how to update and delete documents 
#   in a MongoDB database instance through Python and pymongo
# Resources:
#   buwebdev, Professor Krasso, Bellevue University
#   GeeksforGeeks - find_one query
#     https://www.geeksforgeeks.org/python-mongodb-find_one-query/
# ===========================================

# import statements
from pymongo import MongoClient
import pprint
import datetime

# connect to MongoDB instance
client = MongoClient("localhost", 27017) 
db = client.web335

# update document 
db.users.update_one(
  {"employee_id": "007"},
  {
    "$set": {
      "email": "skerrey@my365.bellevue.edu"
    }
  }
)

# return specific fields
pprint.pprint(db.users.find_one({"employee_id": "007"}, {"email": 1, "employee_id": 1, "first_name": 1, "last_name": 1}))