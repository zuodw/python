from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired

'''
To define a form, one makes a subclass of Form and defines the fields declaratively as class attributes:
'''
class LoginForm(FlaskForm):
    '''
    label – The label of the field.
    validators – A sequence of validators to call when validate is called.
    '''
    username = StringField(label='username', validators=[DataRequired()])
    password = PasswordField(label='password', validators=[DataRequired()])