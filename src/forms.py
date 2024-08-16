from flask_wtf import FlaskForm
from wtforms.validators import DataRequired 
from wtforms import StringField, EmailField, PasswordField, SubmitField





class LoginForm(FlaskForm):
    email = EmailField("email", render_kw={"placeholder":"Escreva o seu email"}, validators=[DataRequired()])
    password = PasswordField("senha", render_kw={"placeholder":" Escreva a sua senha"}, validators=[DataRequired()])
    submit = SubmitField("Fazer Login")




class SigninForm(FlaskForm):
    name = StringField("name", render_kw={"placeholder":"Enter your name"}, validators=[DataRequired()])
    surname = StringField("surname", render_kw={"placeholder":"Enter your surname"}, validators=[DataRequired()])
    
    # FIXME: Enter the date Field
    #birthday = 
    email = EmailField("email", render_kw={"placeholder":"Enter your email"})
    password = PasswordField("password", render_kw={"placeholder":"Type your password"}, validators=[DataRequired()]) 
    check_password = PasswordField("retype password", render_kw={"placeholder":"Re-type your password"}, validators=[DataRequired()])

    submit = SubmitField("Registrar")

