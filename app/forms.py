from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, EqualTo, Email


class AddproductForm(FlaskForm):
    """Addproduct Form"""
    product_name = StringField('Product Name', validators=[DataRequired(), Length(1,64)])
    product_description = StringField('Product Description', validators=[DataRequired()])
    available_stock = SelectField(u'Available Stock', choices=[('1', '1'), ('12', '5'), ('12', '12'), ('12', '20')])
    submit = SubmitField('Add Product')

class RegisterForm(FlaskForm):
    """Register Form"""
    username = StringField('Username', validators=[DataRequired(), Length(1,64)])
    email = StringField('Email', validators=[DataRequired(), Length(1,64), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

