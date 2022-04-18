#!/data/test/python/venv/bin/python3

#from classes.Time import Time 
#import time
#from datetime import datetime

import peewee 
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello world'

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
