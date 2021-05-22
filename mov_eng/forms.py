from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import Email,Length,EqualTo,DataRequired,ValidationError
from mov_eng.database import user

#This is the code for the registration form as well as it takes care of validation of details entered

class RegisterForm(FlaskForm):

    def validate_username(self,username_to_check):
        user2 = user.query.filter_by(username=username_to_check.data).first()
        if user2:
            raise ValidationError('Username alreasy exists try another')

    def validate_emailaddress(self,email_to_check):
        ea2 = user.query.filter_by(email_address=email_to_check.data).first()
        if ea2:
            raise ValidationError('Email Address already exists please log in')

    username = StringField(label='User Name:',validators=[Length(min=2,max=30), DataRequired()])
    email_address = StringField(label='Email:',validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password:',validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirm Password:',validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create Account')

#This is the code for the Login form as well as it takes care of validation of details entered
class LoginForm(FlaskForm):
    username = StringField(label='User Name:',validators=[DataRequired()])
    password = PasswordField(label='Password:',validators=[DataRequired()])
    submit = SubmitField(label='Log in')
