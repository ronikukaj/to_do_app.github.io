from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Length, DataRequired

class SubmitForm(FlaskForm):
    item_field = StringField('Item')
