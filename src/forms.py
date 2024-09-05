from flask_wtf import FlaskForm
from wtforms.validators import DataRequired 
from wtforms import StringField, EmailField, PasswordField, SubmitField,SelectField
from flask_ckeditor import CKEditorField




class LoginForm(FlaskForm):
    email = EmailField("email", render_kw={"placeholder":"Escreva o seu email"}, validators=[DataRequired()])
    password = PasswordField("senha", render_kw={"placeholder":" Escreva a sua senha"}, validators=[DataRequired()])
    submit = SubmitField("Login")




class SigninForm(FlaskForm):
    name = StringField("name", render_kw={"placeholder":"Enter your name"}, validators=[DataRequired()])
    surname = StringField("surname", render_kw={"placeholder":"Enter your surname"}, validators=[DataRequired()])
    
    # FIXME: Enter the date Field
    #birthday = 
    email = EmailField("email", render_kw={"placeholder":"Enter your email"})
    password = PasswordField("password", render_kw={"placeholder":"Type your password"}, validators=[DataRequired()]) 
    check_password = PasswordField("retype password", render_kw={"placeholder":"Re-type your password"}, validators=[DataRequired()])

    submit = SubmitField("Registrar")





class PostForm(FlaskForm):
    # TODO: Criar um formulário, que sere para criar nossos post,s isso pode ser feito com o usod da biblioteca markdown 
    # para facilitar como os posts são feitos
    title = StringField("title", render_kw={"placeholder":"Título do post"}, validators=[DataRequired()])
    description = StringField("description", render_kw={"placeholder":"Descrição rápida do post"}, validators=[DataRequired()])
    content = CKEditorField("content", validators=[DataRequired()])
    submit = SubmitField("Enviar") 
