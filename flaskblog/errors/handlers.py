from flask import Blueprint, render_template,url_for
from flask_login import current_user

errors = Blueprint('errors', __name__)


@errors.app_errorhandler(404)
def error_404(error):
    if current_user.is_authenticated:
        image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('errors/404.html', **locals()), 404


@errors.app_errorhandler(403)
def error_403(error):
    if current_user.is_authenticated:
        image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('errors/403.html', **locals()), 403


@errors.app_errorhandler(500)
def error_500(error):
    if current_user.is_authenticated:
        image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('errors/500.html', **locals()), 500
