from flask_wtf import FlaskForm
from wtforms import  StringField, TextAreaField, SelectField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import DataRequired

class propertyForm(FlaskForm):
    title = StringField('Property Title', validators=[DataRequired()])
    bedrooms = StringField('No. of Bedrooms', validators=[DataRequired()])
    bathrooms = StringField('No. of Bathrooms', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    price = StringField('Price', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    type = SelectField('Property Type', choices=[("House","House"),("Apartment", "Apartment")])
    photo = FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'Images only!'])])