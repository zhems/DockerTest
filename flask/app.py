from flask import Flask, request
from pymongo import MongoClient
import pymongo
app = Flask(__name__)

@app.route('/')
def hello_geek():
    def query_mongo_latest(db_name, collection_name, number = 1, mongo_uri = 'mongodb://192.168.4.37:27017/?directConnection=true'):
        client = MongoClient(mongo_uri)
        db = client[db_name]
        collection = db[collection_name]
        if number == 1:
            res = collection.find_one(sort=[( '_id', pymongo.DESCENDING )])
        else:
            res = collection.aggregate([{'$sort': {'_id': -1}},{'$limit': number}])
            res = list(res)
        return res
    # return '<h1>' + str(query_mongo_latest('pddDB','acmvReadings')) + '</h2>'
    return '<h1>Hello from Flask & Docker</h2>'

@app.route("/api",  methods = ['POST'])
def api_insert():
    print(request.args)
    return "Success: Book information has been added."

if __name__ == "__main__": #port 5000, host='0.0.0.0'
    app.run(debug=True, port=5229)