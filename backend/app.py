# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
  return '<h1>Hello World!</h1>'

@app.route('/application')
def index():
  return 'Hello'

if __name__ == '__main__':
  app.run()
