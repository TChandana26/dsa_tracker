from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

user_db = client['user_db']
problem_db = client['problem_db']


user_col = user_db['users']
problem_col = problem_db['problems']
