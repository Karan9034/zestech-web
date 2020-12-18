from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, IntegerField, TextAreaField, BooleanField, FileField
from wtforms.validators import DataRequired, Email, Length, NumberRange
from flask_mail import Message
import os, magic

class QueryForm(FlaskForm):
	email = StringField('Email*', validators=[DataRequired(), Email()])
	phone = IntegerField('Phone*', validators=[DataRequired(), NumberRange(min=1000000000, max=9999999999)])
	address = StringField('Address*', validators=[DataRequired(), Length(min=10, max=1000)])
	bill = IntegerField('Average Monthly Bill*', validators=[DataRequired()])
	message = TextAreaField('Message')
	files = FileField('Attachments', render_kw={"multiple":"True", "id":"upload"})
	promotion = BooleanField('Promotional')
	submit = SubmitField('Get Quote')

from app import mail, app

def send_mail(form):
	msg = Message("Quote Enquiry Mail", sender='inquiry.zestech@gmail.com', recipients=['karan.agr9034@gmail.com'])
	msg.body = f'''Email: {form.email.data}
Phone: {form.phone.data}
Address: {form.address.data}
Average Monthly Bill: {form.bill.data}
Message: {form.message.data}
'''
	for file in os.listdir(os.path.join(os.getcwd(), 'files')):
		with app.open_resource(os.path.join(os.getcwd(), 'files', file)) as fp:
			mime = magic.Magic(mime=True)
			c_type = mime.from_file(os.path.join(os.getcwd(), 'files', file))
			msg.attach(file, c_type, fp.read())
	mail.send(msg)