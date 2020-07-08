from flask import Flask
from flask import Flask, render_template, jsonify, flash, request
from flaskext.mysql import MySQL
#from werkzeug import generate_password_hash, check_password_hash
import db_curd.ops as dbops
 
app = Flask(__name__)
mysql = MySQL()
 
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '1Blue8eagle!234'
app.config['MYSQL_DATABASE_DB'] = 'test'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route("/")
def main():
    conn = mysql.connect()
    cursor = conn.cursor()
    #_hashed_password = generate_password_hash(_password)
    return render_template('index.html')    

@app.route('/listUsers')
def listUsers():
    dbops.read_records()

    
if __name__ == "__main__":
    app.debug = True
    app.run()
