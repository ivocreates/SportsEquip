from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, FloatField, IntegerField, SelectField, HiddenField
from wtforms.validators import DataRequired, Email, EqualTo, Length, NumberRange

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    password2 = PasswordField('Confirm Password', 
                              validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

class ProductForm(FlaskForm):
    name = StringField('Product Name', validators=[DataRequired(), Length(max=100)])
    description = TextAreaField('Description', validators=[DataRequired()])
    price = FloatField('Price', validators=[DataRequired(), NumberRange(min=0.01)])
    category = SelectField('Category', choices=[
        ('football', 'Football'),
        ('basketball', 'Basketball'),
        ('tennis', 'Tennis'),
        ('soccer', 'Soccer'),
        ('baseball', 'Baseball'),
        ('golf', 'Golf'),
        ('fitness', 'Fitness'),
        ('running', 'Running'),
        ('swimming', 'Swimming'),
        ('cycling', 'Cycling'),
        ('other', 'Other')
    ], validators=[DataRequired()])
    image_url = StringField('Image URL')
    stock_quantity = IntegerField('Stock Quantity', validators=[DataRequired(), NumberRange(min=0)])
    submit = SubmitField('Save Product')

class ReviewForm(FlaskForm):
    rating = SelectField('Rating', choices=[
        (5, '5 Stars'),
        (4, '4 Stars'),
        (3, '3 Stars'),
        (2, '2 Stars'),
        (1, '1 Star')
    ], coerce=int, validators=[DataRequired()])
    comment = TextAreaField('Comment', validators=[Length(max=500)])
    product_id = HiddenField('Product ID', validators=[DataRequired()])
    submit = SubmitField('Submit Review')

class UpdateOrderStatusForm(FlaskForm):
    status = SelectField('Status', choices=[
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled')
    ], validators=[DataRequired()])
    submit = SubmitField('Update Status')
