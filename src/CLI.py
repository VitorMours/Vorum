import click
from flask.cli import with_appcontext
from random import choice, randint
import string
import secrets
from .models import db, User, Post

# Função para gerar string aleatória
def generate_random_string(length=10):
    return ''.join(choice(string.ascii_letters + string.digits) for _ in range(length))

# Função para gerar nome aleatório
def generate_random_name():
    first_name = generate_random_string(5).capitalize()
    last_name = generate_random_string(7).capitalize()
    return f"{first_name} {last_name}"

# Função para gerar e-mail aleatório
def generate_random_email():
    return f"{generate_random_string(5)}@example.com"

# Função para criar um usuário fictício
def create_user():
    name = generate_random_name()
    email = generate_random_email()
    password = secrets.token_urlsafe(13)
    return [name, email, password]

# Função para criar post fictício
def create_post():
    title = generate_random_string(10)
    description = generate_random_string(20)
    content = generate_random_string(100)
    return [title, description, content]

@click.command(name="create-fake-users")
@click.argument("quantity")
@with_appcontext
def create_fake_users(quantity):
    for _ in range(int(quantity)):
        data = create_user()
        fullname = data[0].split()
        name = fullname[0]
        surname = fullname[-1]
        email = data[1]
        password = data[2]

        user = User(
            name=name,
            surname=surname,
            email=email,
            password=password
        )     
        db.session.add(user)

    db.session.commit()
    print(f"{quantity} usuários falsos foram criados.")

@click.command(name="create-fake-posts")
@click.argument("quantity")
@with_appcontext 
def create_fake_posts(quantity):
    for _ in range(int(quantity)):
        data = create_post()
        post = Post(
            title=data[0],
            description=data[1],
            content=data[2]
        )
        db.session.add(post)

    db.session.commit()
    print(f"Foram criadas um total de {quantity} postagens.")

@click.command(name="delete-all-users")
@with_appcontext 
def delete_all_users():
    print(f"Temos um total de {User.query.count()} usuários na base de dados.")
    print(f"Deletando {User.query.delete()} usuários.")
    db.session.commit()
    print(f"Temos um total de {User.query.count()} usuários após a exclusão.")

@click.command(name="delete-all-posts")
@with_appcontext 
def delete_all_posts():
    print(f"Temos um total de {Post.query.count()} postagens na base de dados.")
    print(f"Deletando {Post.query.delete()} postagens.")
    db.session.commit()
    print(f"Total de postagens após a exclusão: {Post.query.count()}")
