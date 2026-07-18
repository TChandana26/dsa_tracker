from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

print("MONGO_URI:", os.getenv("MONGO_URI"))

client = MongoClient(os.getenv("MONGO_URI"),serverSelectionTimeoutMS=5000)




try:
    client.admin.command("ping")
    print("✅ Connected to MongoDB Atlas!")
except Exception as e:
    print("❌", e)


user_db = client['user_db']
problem_db = client['problem_db']


user_col = user_db['users']
problem_col = problem_db['problems']
