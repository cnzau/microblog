from flask import render_template
from app import app
#route decorators create the mappings from URLs / and /index to this function.
@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Clement'} #placeholder user object(fake/mock user object)
    posts = [  # fake array of posts
        { 
            'author': {'nickname': 'John'}, 
            'body': 'Beautiful day in Portland!' 
        },
        { 
            'author': {'nickname': 'Susan'}, 
            'body': 'The Avengers movie was so cool!' 
        },
        { 
            'author': {'nickname': 'Timothy'}, 
            'body': 'The ever evolving technology!' 
        },
        { 
            'author': {'nickname': 'Nzau'}, 
            'body': 'Music is a healing for the soul!' 
        }
    ]
    #displayed on the client's web browser
    #render_template invokes the Jinja2 templating engine
    #Jinja2 substitutes {{...}} blocks with the corresponding values provided as template arguments.
    return render_template('index.html',
                           user=user,
    	                   posts=posts)
