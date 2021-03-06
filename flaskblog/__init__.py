from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flaskblog.config import Config
from flask_moment import Moment
from .momentjs import momentjs
# import sqlalchemy


db = SQLAlchemy()




# # The SQLAlchemy engine will help manage interactions, including automatically
# # managing a pool of connections to your database
# db = sqlalchemy.create_engine(
#     # Equivalent URL:
#     # postgres+pg8000://<db_user>:<db_pass>@/<db_name>?unix_sock=/cloudsql/<cloud_sql_instance_name>/.s.PGSQL.5432
#     sqlalchemy.engine.url.URL(
#         drivername='postgres+pg8000',
#         username='postgres',
#         password='newton' ,
#         database='newton_wiki',
#         query={
#             'unix_sock': '/cloudsql/{}/.s.PGSQL.5432'.format(
#                 # 'oauth-347106:us-central1:newtonwiki'
#                 cloud_sql_connection_name)
#         }
#     ),
#     # ... Specify additional properties here.
#     # ...
# )









bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
mail = Mail()
moment = Moment()


def create_app(config_class=Config):
    application = Flask(__name__)
    application.config.from_object(Config)

    db.init_app(application)
    bcrypt.init_app(application)
    login_manager.init_app(application)
    mail.init_app(application)
    moment.init_app(application)

    from flaskblog.users.routes import users
    from flaskblog.posts.routes import posts
    from flaskblog.main.routes import main
    from flaskblog.errors.handlers import errors
    application.register_blueprint(users)
    application.register_blueprint(posts)
    application.register_blueprint(main)
    application.register_blueprint(errors)

    return application

    application.jinja_env.globals['momentjs'] = momentjs
