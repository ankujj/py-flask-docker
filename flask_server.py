from flask import Flask, request, render_template
import pymongo
import os

app=Flask(__name__)
""""
@app.route("/")
@app.route("/<username>")
def say_Hello(username):
    if username!="":
        return f"Hello {username}"
    else:
        return "Hello user, please send your name"

"""


@app.route("/")
def say_hello() -> "html":
    return render_template("index.html")

@app.route("/<username>")
def say_hello_to_user(username) -> str:
    return f"Hello {username} from the python world"

@app.route("/addUser",methods=["GET","POST"])
def add_user():
    request_data=request.get_json()
    print(f"Request data {request_data}")

    mongo_db_url=os.getenv("MONGO_DB_URL")
    print(f"Read the MONGO_DB_URL as [{mongo_db_url}]")

    
    if mongo_db_url is None:
        mongo_db_url="mongodb://root:root@localhost:27017"

    print(f"Connecting to MONGO DB at {mongo_db_url}")
    mongo_client=pymongo.MongoClient(mongo_db_url)
    mongo_db=mongo_client["user_db"]
    mongo_collection=mongo_db["users"]
    mongo_insert_ret=mongo_collection.insert_one(request_data)
    return f"Your details are updated {request_data['name']} with id as {mongo_insert_ret.inserted_id}"