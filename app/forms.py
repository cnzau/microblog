from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class LoginForm(Form):
	#OpenIDs benefit- authentication is done by the provider of the OpenID
	#we don't have to validate passwords, which makes our site more secure to our users.
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)