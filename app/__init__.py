from flask import Flask

app = Flask(__name__)
#Import at views the end and not the beginning of the script to avoid circular references.
#The views module needs to import the app variable defined in this script.
from app import views