from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField,FileField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    picture = FileField('Upload Post Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Post')
