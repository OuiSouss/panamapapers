from flask_wtf import FlaskForm
from wtforms.fields import *
from wtforms.validators import Required, Email


class SignupForm(FlaskForm):
    name = TextField(u'Your name', validators=[Required()])
 

    submit = SubmitField(u'Signup')
