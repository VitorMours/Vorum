from flask import Flask 
from .views import views
from .models import db
from flask_migrate import Migrate

def create_app():
    app = Flask(__name__, template_folder="templates")

    app.config.from_mapping(
        SECRET_KEY="dev",
        SQLALCHEMY_DATABASE_URI="sqlite:///database.sqlite3"
    )

    db.init_app(app)
    migrate = Migrate(app, db)

    with app.app_context():
        db.create_all()

    app.register_blueprint(views)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run()
