import click
from flask.cli import with_appcontext
from .utils import mock_posts as mock
from .models import db, User, Post
@click.command(name="create-fake-users")
@with_appcontext
def create_fake_users():
          data = mock.create_user()
          print(data)


@click.command(name="create-fake-posts")
@with_appcontext 
def create_fake_posts():
          data = mock.create_post()
          




@click.command(name="delete-all-users")
@with_appcontext 
def delete_all_users():
          print(f"Temos um total de elementos: {User.query.count()} dentro da base de dados")
          print(User.query.delete())
          db.session.commit()
          print(f"Temos um total de elementos: {User.query.count()} dentro da base de dados depois de modificar")



