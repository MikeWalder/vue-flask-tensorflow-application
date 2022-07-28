# app.py
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
  return '<h1>Hello World!</h1>'

@app.route('/tensor', methods=['GET', 'POST'])
def receive_datas():
    return 'This is our first TensorFlow application !!'

if __name__ == '__main__':
  app.run()
