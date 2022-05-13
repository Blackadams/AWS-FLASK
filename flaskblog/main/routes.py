from flask import render_template, request, Blueprint, url_for, flash, redirect
from flask_login import login_user, current_user, logout_user, login_required
from flaskblog.models import Post
from flaskblog.main.forms import AmountForm

main = Blueprint('main', __name__)



#  from exts import db # or wherever you keep your sqlalchemy instance 
#  from flask_login import current_user
#  from pytz import UTC
#  from datetime import datetime 

# @app.before_request
# def update_last_seen():
#     if current_user.is_authenticated:
#         current_user.last_seen = datetime.now(tzinfo=UTC) #utcnow doesn't actually attach a timezone
#         db.session.add(current_user) 
#         db.session.commit()



@main.route("/")
@main.route("/home/")
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=1)

    ipaddress = request.remote_addr

    if current_user.is_authenticated:
        image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('try.html', **locals())


@main.route('/fe/')
def fe():
  flash("Well, that was more popular than we thought. All guests must be accompanied by a member. ", 'success')


  return redirect(url_for('main.home'))


