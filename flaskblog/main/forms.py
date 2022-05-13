from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField,FileField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired


class AmountForm(FlaskForm):
    amount = StringField('Mail me nothing at', validators=[DataRequired()])
    submit = SubmitField('Pay')
