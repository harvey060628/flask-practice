from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class MessageForm(FlaskForm):
    name = StringField('What is your name ?', validators=[DataRequired()])
    text = StringField('Leave some message ~')
    submit = SubmitField('Submit')

