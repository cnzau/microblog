#!flask/bin/python
#import the app variable from our app package and invoke its run method to start the server
#app variable holds the Flask instance that we created
from app import app
app.run(debug=True)
