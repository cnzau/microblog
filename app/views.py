from app import app
#route decorators create the mappings from URLs / and /index to this function.
@app.route('/')
@app.route('/index')
def index():
    #displayed on the client's web browser
    return "Hello, World!"