from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length


class MessageForm(FlaskForm):
    name = StringField('What is your name ?', validators=[DataRequired()])
    text = StringField('Leave some message ~')
    submit = SubmitField('Submit')

# class LoginForm(FlaskForm):
#     username = StringField('Username', validators=[DataRequired(), Length(1, 20)])
#     password = PasswordField('Password', validators=[DataRequired(), Length(8, 150)])
#     remember = BooleanField('Remember me')
#     submit = SubmitField()
