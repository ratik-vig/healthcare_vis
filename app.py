from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)

@app.route('/')
def index():
    client = MongoClient("mongodb://localhost:27017/")
    db = client['healthcare']
    collection = db['test']
    data = list(collection.find({}, {'_id': 0}))

    collection2 = db['bmi_diabetes']
    data2 = list(collection2.find({}, {'_id': 0}))

    collection3 = db['cholesterol_diabetes']
    data3 = list(collection3.find({}, {'_id': 0}))

    collection4 = db['smoking_drinking']
    data4 = list(collection4.find({}, {'_id': 0}))

    collection5 = db['heart_stroke']
    data5 = list(collection5.find({}, {'_id': 0}))

    collection6 = db['highbp_diabetes']
    data6 = list(collection6.find({}, {'_id': 0}))

    return render_template('chart.html', data=[data, data2, data3, data4, data5, data6])

if __name__ == '__main__':
    app.run(debug=True)
