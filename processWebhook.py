import flask
import os
from flask import send_from_directory

import psycopg2 
import psycopg2.extras
import re 

app = flask.Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    
    DB_HOST = "ec2-34-224-239-147.compute-1.amazonaws.com"
    DB_NAME = "d4208faaa1c8ck"
    DB_USER = "ranbbcmbtqhcao"
    DB_PASS = "4c74edd940a5b6d200359899004e41e362b0d72fa16b9d5d35aae794dcbbec6b"
 
    conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)

    cur = conn.cursor()

    cur.execute("SELECT * from a_usuario")
    
    test = cur.fetchone()
    
    print(test)
    
    return test[1]

if __name__ == "__main__":
    app.secret_key = 'ItIsASecret'
    app.debug = True
    app.run()