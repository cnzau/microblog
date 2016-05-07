from flask import Flask

app = Flask(__name__)
#set Flask to read and use the config file
app.config.from_object('config')
#Import at views the end and not the beginning of the script to avoid circular references.
#The views module needs to import the app variable defined in this script.
from app import views