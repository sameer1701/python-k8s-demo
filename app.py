import os
from flask import Flask

# from flask.ext.mysql import MySQL   # For older versions of flask-mysql
app = Flask(__name__)



@app.route("/")
def main():
    return "Welcome!"


@app.route('/health')
def hello():
    return 'I am good, how about you?'



if __name__ == "__main__":
    app.run()
