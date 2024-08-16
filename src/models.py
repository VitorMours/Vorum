from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey, String, Integer 
from sqlalchemy.orm import mapped_column, Mapped
#from sqlalachemy_utils import EmailType


db = SQLAlchemy()

class User(db.Model):
        __tablename__="User"

        id: Mapped[int] = db.Column(Integer, primary_key=True)
        name: Mapped[str] = db.Column(String(40)) 
        surname: Mapped[str] = db.Column(String(60))
        email: Mapped[str] = db.Column(String(120), unique=True)
        password: Mapped[str] = db.Column(String(30))

        def __str__(self):
                return f"User information: \n\tname:{self.name} \n\tsurname:{self.surname} \n\temail:{self.email}"


class Post(db.Model): 
          __tablename__= "Post"

          id: Mapped[int] = db.Column(Integer, primary_key=True)
          owner: Mapped[User] = db.Column(Integer, ForeignKey('User.id'), nullable=False)
          content: Mapped[str] = db.Column(String(200)) 



