from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from flaskblog import db, login_manager
from flask_login import UserMixin, AnonymousUserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)
    # member_since = db.Column(db.DateTime(), default=datetime.utcnow)
    # balance = db.Column(db.Float, nullable=True, default=0)
    # logs = db.Column(db.String)
    # PhNo = db.Column(db.Integer, unique=True

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    # post_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    # hidden = db.Column(db.Boolean, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"


# class Comment(db.Model):
#     __tablename__ = 'comments'
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
#     post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
#     comment = db.Column(db.String(1024))
#     create_timestamp = db.Column(db.DateTime, default=datetime.now())
#     edit_timestamp = db.Column(db.DateTime, default=datetime.now())
#     deleted = db.Column(db.Boolean, default=0)

#     def __init__(self, book, user, comment):
#         self.user = user
#         self.book = book
#         self.comment = comment
#         self.create_timestamp = datetime.now()
#         self.edit_timestamp = self.create_timestamp
#         self.deleted = 0


# class Log(db.Model):
#     __tablename__ = 'logs'
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
#     book_id = db.Column(db.Integer, db.ForeignKey('books.id'))
#     borrow_timestamp = db.Column(db.DateTime, default=datetime.now())
#     return_timestamp = db.Column(db.DateTime, default=datetime.now())
#     returned = db.Column(db.Boolean, default=0)

#     def __init__(self, user, book):
#         self.user = user
#         self.book = book
#         self.borrow_timestamp = datetime.now()
#         self.return_timestamp = datetime.now() + timedelta(days=30)
#         self.returned = 0

#     def __repr__(self):
#         return u'<%r - %r>' % (self.user.name, self.book.title)