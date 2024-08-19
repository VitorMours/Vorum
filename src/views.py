from flask import Blueprint, redirect, render_template, request, session, url_for, flash
from .forms import LoginForm, SigninForm, PostForm
from .models import User, db
from .utils.auth import login_required

views = Blueprint("views", __name__, template_folder="templates", static_folder="static")





@views.route('/')
def index():
    return render_template("index.jinja")


@views.route('/register', methods=["GET","POST"])
def register():

    form = SigninForm()

    if request.method == "GET":
        return render_template("register.jinja", form=form)

    elif request.method == "POST":

        if form.validate_on_submit():
            name = request.form["name"]
            surname = request.form["surname"]
            email = request.form["email"]
            password = request.form["password"]
            check_password = request.form["check_password"]

            if password != check_password:
                flash("Você precisa que a senhas duas senhas inseridas, sejam iguais", "warning")
                return redirect(url_for('views.register'))

            elif user := User.query.filter_by(email=email).first() is None:
                user = User(
                        name = name,
                        surname = surname, 
                        email = email, 
                        password = password
                        )

                db.session.add(user)
                db.session.commit()
                flash("Usuário cadastrado", "sucess")
                session['logged_in'] = True

                return redirect(url_for('views.index'))

            else:
                flash("Já existe um usuário com esse cadastro dentro da base de dados", "danger")
                return redirect(url_for('views.register'))

    else:
        return redirect(url_for("views.error"))


@views.route('/login', methods=["GET","POST"])
def login():

    form = LoginForm()
    if request.method == "GET":
        return render_template("login.jinja", form=form)

    elif request.method == "POST":
        if form.validate_on_submit():
            email = request.form["email"]
            password = request.form["password"]

            print(email, password)
            
            if (user := User.query.filter_by(email=request.form["email"]).first()) is None:

                flash("Esse usuário não existe dentro da base de dados, você entretanto pode criar esse usuário", "danger")
                return redirect(url_for("views.login"))
            
            else:
                if user.password == password:


                    session['logged_in'] = True
                    flash("Usuário logado","sucess")

                    return redirect(url_for("views.index"))
                
                else:

                    flash("Credential do usuário errada", "warning")
                    return redirect(url_for("views.login"))
            
    else:
        return redirect(url_for("views.invalid_method"))


@views.route('/create_post', methods=["GET", "POST"])
@login_required
def create_post():
    if request.method == "GET":

        form = PostForm()
        return render_template("create_post.jinja", form=form)

    elif request.method == "POST":

        if form.validate_on_submit():
            title = request.form["title"]
            content = request.form["content"]
            description = request.form["description"]


        return redirect(url_for("views.index"))

    else:
        return redirect(url_for("views.invalid_method"))




@views.app_errorhandler(404)
def page_not_found(error):
    return render_template("error/404.jinja"), 404

@views.app_errorhandler(405)
def invalid_method(error):
    return render_template("error/405.jinja"), 405





@views.route('/logout')
@login_required
def logout():
    session.pop("logged_in", None)
    return redirect(url_for("views.index"))
