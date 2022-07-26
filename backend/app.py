# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
  return '<h1>Hello World!</h1>'

@app.route('/application')
def index():
  return 'Hello there'

if __name__ == '__main__':
  app.run()
