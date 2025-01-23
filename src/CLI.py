import click
from flask.cli import with_appcontext
from .utils import mock_posts as mock
from .models import db, User, Post

@click.command(name="create-fake-users")
@click.argument("quantity")
@with_appcontext
def create_fake_users(quantity):

        for _ in range(int(quantity)):

            data = mock.create_user()
            fullname: list[str] = data[0].split()
            name: str = fullname[0]
            surname: str = fullname[-1]
            email: str = data[1]
            senha: int = data[2]

            user = User(
                name = name,
                surname = surname,
                email = email,
                password = senha
            )     
            db.session.add(user)

        db.session.commit()

@click.command(name="create-fake-posts")
@click.argument("quantity")
@with_appcontext 
def create_fake_posts(quantity):

    
    for _ in range(int(quantity)):
        data = mock.create_post()
        post = Post(title=data[0],
                          description=data[1],
                          content=data[2]
                          )
        db.session.add(post)

            
    db.session.commit()
    print(f"Foram criadas um total de: {quantity} postagens")


@click.command(name="delete-all-users")
@with_appcontext 
def delete_all_users():
    print(f"Temos um total de elementos: {User.query.count()} dentro da base de dados")
    print(User.query.delete())
    db.session.commit()
    print(f"Temos um total de elementos: {User.query.count()} dentro da base de dados depois de modificar")



@click.command(name="delete-all-posts")
@with_appcontext 
def delete_all_posts():

    print("Deletando todos os post presentes dentro da base de dados")
    print(Post.query.delete())
    db.session.commit()
    print(f"Total de posts presente na base de dados:{Post.query.count()}")

