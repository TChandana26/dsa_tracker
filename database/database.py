from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(os.getenv("MONGO_URI"))

user_db = client['user_db']
problem_db = client['problem_db']


user_col = user_db['users']
problem_col = problem_db['problems']
