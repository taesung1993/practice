from pymongo import MongoClient
from flask import Flask, render_template

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbsparta

@app.route('/')
def home():
    musics = list(db.musics.find())
    return render_template('index.html', musics=musics)

if __name__ == '__main__':
    print(__name__)
    app.run('localhost', port = 5000, debug = True)
