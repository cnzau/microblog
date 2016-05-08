from flask import render_template, flash, redirect
from app import app
#import LoginForm class, instantiate an object from it
from .forms import LoginForm
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

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
              (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html',
                           title='Sign In',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])