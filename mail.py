from flask_mail import Message
import os, magic

def send_mail(form):
	msg = Message("Quote Enquiry Mail", sender='inquiry.zestech@gmail.com', recipients=['karan.agr9034@gmail.com'])
	msg.body = f'''Email: {form.email.data}
Phone: {form.phone.data}
Address: {form.address.data}
Average Monthly Bill: {form.bill.data}
Message: {form.message.data}
'''
	for file in os.listdir(os.path.join(os.getcwd(), 'files')):
		with open(os.path.join(os.getcwd(), 'files', file)) as fp:
			mime = magic.Magic(mime=True)
			c_type = mime.from_file(os.path.join(os.getcwd(), 'files', file))
			msg.attach(file, c_type, fp.read())
	return msg