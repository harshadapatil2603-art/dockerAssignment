from Flask import Flask, render_template, request
from datetime import datetime
from dotenv import load_dotenv
import os
import pymongo

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

Client = pymongo.MongoClient(MONGO_URI)

db = client.test

collection = db["flask-tutorial"]

app = Flask(__name__)

@app.route('/')
def home():

    day_of_week = datetime.today().strftime('%A')

    current_time = datetime.now().strftime('%H:%M:%S')

    return render_template('index.html', day_of_week=day_of_week, current_time=current_time)

@app.route('/submit', methods=['POST'])
def submit():
    
    form_data = dict(request.form)

    collection.insert_one(form_data)

    return 'Data submitted successfully!'

@app.route('/view')
def view():

    data = collection.find()

    data = list(data)

    for item in data:

        print(item)
        del item['_id']

    data = {
        'data': data
    }  

    return data 

if __name__ == '__main__':
    app.run(debug=True)
    
      


