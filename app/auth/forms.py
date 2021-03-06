# Import Form and RecaptchaField (optional)
from flask_wtf import FlaskForm

# Import Form elements such as TextField and BooleanField (optional)
from wtforms import StringField, PasswordField

# Import Form validators
from wtforms.validators import DataRequired, Email


# Define the login form (WTForms)

class LoginForm(FlaskForm):
    # email = StringField('Email Address', [Email(), DataRequired(message='Forgot your email address?')])
    # password = PasswordField('Password', [DataRequired(message='Must provide a password. ;-)')])
    email = StringField('Email Address', [])
    password = PasswordField('Password', [])
