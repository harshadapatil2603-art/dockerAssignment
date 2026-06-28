from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
CORS(app)

client = MongoClient(os.getenv("MONGO_URI"))

db = client[os.getenv("DB_NAME")]
collection = db[os.getenv("COLLECTION")]

@app.route("/submit", methods=["POST"])
def submit():

    try:

        data = request.json

        document = {
            "itemName": data["itemName"],
            "itemDescription": data["itemDescription"]
        }

        collection.insert_one(document)

        return jsonify({
            "success": True,
            "message": "Data submitted successfully"
        })

    except Exception as e:

        return jsonify({
            "success": False,
            "message": str(e)
        }),500


if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000)