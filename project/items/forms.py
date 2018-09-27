from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired


class AddItemForm(Form):
    item_title = StringField('Item Title', validators=[DataRequired()])
    item_description = StringField('Item Description', validators=[DataRequired()])
    item_comment = StringField('Item Comment', validators=[DataRequired()])
