from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField, SubmitField, IntegerField
from wtforms.validators import DataRequired
# from flask_wtf.file import FileAllowed

class BooksForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    pages = IntegerField('Pages', validators=[DataRequired()])
    image = FileField('Cover Photo')