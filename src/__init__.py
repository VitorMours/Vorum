from flask import Flask 
from .views import views
from .models import User, db
from flask_migrate import Migrate
from flask_ckeditor import CKEditor
from .CLI import *
ckeditor = CKEditor()

def create_app():
    app = Flask(__name__, template_folder="templates")

    app.config.from_mapping(
        SECRET_KEY="dev",
        TEMPLATE_AUTO_RELOAD=True,
        SQLALCHEMY_DATABASE_URI="sqlite:///database.sqlite3"
    )

    db.init_app(app)
    ckeditor.init_app(app)
    migrate = Migrate(app, db)

    with app.app_context():
        db.create_all()



    app.register_blueprint(views)



    app.cli.add_command(CLI.create_fake_users)
    app.cli.add_command(CLI.delete_all_users)


    return app

if __name__ == "__main__":
    app = create_app()
    app.run()




