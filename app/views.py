from flask import render_template
from app import app
#route decorators create the mappings from URLs / and /index to this function.
@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Clement'} #placeholder user object(fake/mock object)
    #displayed on the client's web browser
    #render_template invokes the Jinja2 templating engine
    #Jinja2 substitutes {{...}} blocks with the corresponding values provided as template arguments.
    return render_template('index.html',
                           user=user)
