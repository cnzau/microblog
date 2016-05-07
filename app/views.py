from app import app
#route decorators create the mappings from URLs / and /index to this function.
@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Clemmo'} #placeholder user object(fake/mock object)
    #displayed on the client's web browser
    return '''
<html>
  <head>
    <title>Home Page</title>
  </head>
  <body>
    <h1>Hello, ''' + user['nickname'] + '''</h1>
  </body>
</html>
'''