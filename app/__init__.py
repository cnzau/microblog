from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
#set Flask to read and use the config file
app.config.from_object('config')
#object that will be our database
db = SQLAlchemy(app)
#Import at views the end and not the beginning of the script to avoid circular references.
#The views module needs to import the app variable defined in this script.
#Import models module
from app import views, models
