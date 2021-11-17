from flask import Flask, request, session, redirect, url_for, render_template, flash
import psycopg2 #pip install psycopg2 
import psycopg2.extras
import re 
from werkzeug.security import generate_password_hash, check_password_hash
 
app = Flask(__name__)
app.secret_key = 'cairocoders-ednalan'
 
DB_HOST = "ec2-34-224-239-147.compute-1.amazonaws.com"
DB_NAME = "d4208faaa1c8ck"
DB_USER = "ranbbcmbtqhcao"
DB_PASS = "4c74edd940a5b6d200359899004e41e362b0d72fa16b9d5d35aae794dcbbec6b"
 
conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)

cur = conn.cursor()

cur.execute("SELECT * from a_usuario")

test = cur.fetchone()

print(test)

@app.route('/')
@app.route('/home')

def home():
    return 'Hello World'
    


