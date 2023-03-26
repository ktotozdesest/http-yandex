from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class Form(FlaskForm):
    username = StringField('id астронафта', validators=[DataRequired()])
    password = PasswordField('Пароль астронафта', validators=[DataRequired()])
    username_2 = StringField('id капитана', validators=[DataRequired()])
    password_2 = PasswordField('Пароль капитана', validators=[DataRequired()])
    submit = SubmitField('Войти')
