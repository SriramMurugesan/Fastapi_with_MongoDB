from pymongo import MongoClient


client = MongoClient("mongodb+srv://sri:sri1909@cluster0.gx1w8ma.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

db = client.todo_db

collection = db["todo_collection"]