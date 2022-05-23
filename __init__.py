from flask import Flask
import pymongo
#from Engineering import routes

app = Flask(__name__)
app.secret_key = "Secret Key"
app.config['SECRET_KEY'] = 'SuperSecretKey'