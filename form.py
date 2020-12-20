from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, IntegerField, TextAreaField, BooleanField, FileField
from wtforms.validators import DataRequired, Email, Length, NumberRange

class QueryForm(FlaskForm):
	email = StringField('Email*', validators=[DataRequired(), Email()])
	phone = IntegerField('Phone*', validators=[DataRequired(), NumberRange(min=1000000000, max=9999999999)])
	address = StringField('Address*', validators=[DataRequired(), Length(min=10, max=1000)])
	bill = IntegerField('Average Monthly Bill*', validators=[DataRequired()])
	message = TextAreaField('Message')
	files = FileField('Attachments', render_kw={"id":"upload"})
	promotion = BooleanField('Promotional')
	submit = SubmitField('Get Quote')
