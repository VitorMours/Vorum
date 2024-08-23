from functools import wraps
from flask import flash, redirect, session, url_for

def login_required(f) -> bool:
    @wraps(f)
    def decorator(*args, **kwargs):
        print("Entrando dentro do decorador")
        if "logged_in" in session and session['logged_in'] == True:
            print(f"Se a sessão está logada: {session['logged_in']}")
            return f(*args, **kwargs)

        else:
            flash("Você precisa primeiro estar logado dentro do sistema para usar a plataforma", "danger")
            return redirect(url_for("views.index"))

    return decorator
