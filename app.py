import os
from flask import Flask
import MySQL  # For newer versions of flask-mysql

# from flask.ext.mysql import MySQL   # For older versions of flask-mysql
app = Flask(__name__)

mysql = MySQL()

mysql_database_host = 'MYSQL_DATABASE_HOST' in os.environ and os.environ['MYSQL_DATABASE_HOST'] or 'localhost'

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = os.environ['MYSQL_DATABASE_USER']
app.config['MYSQL_DATABASE_PASSWORD'] = os.environ['MYSQL_DATABASE_PASSWORD']
app.config['MYSQL_DATABASE_DB'] = os.environ['MYSQL_DATABASE_DB']
app.config['MYSQL_DATABASE_HOST'] = mysql_database_host
mysql.init_app(app)

conn = mysql.connect()

cursor = conn.cursor()


@app.route("/")
def main():
    return "Welcome!"


@app.route('/health')
def hello():
    return 'I am good, how about you?'


@app.route('/fromDb')
def read():
    cursor.execute("SELECT * FROM employees")
    row = cursor.fetchone()
    result = []
    while row is not None:
        result.append(row[0])
        row = cursor.fetchone()

    return ",".join(result)


if __name__ == "__main__":
    app.run()
