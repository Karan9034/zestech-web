from flask_mail import Message
import os, magic

def send_mail(form):
	msg = Message("Quote Enquiry Mail", sender='inquiry.zestech@gmail.com', recipients=['karan.agr9034@gmail.com'])
	msg.body = f'''Email: 
Phone: 
Address:
Average Monthly Bill: 
Message: 
'''
	# for file in os.listdir(os.path.join(os.getcwd(), 'uploads')):
	# 	with open(os.path.join(os.getcwd(), 'uploads', file)) as fp:
	# 		mime = magic.Magic(mime=True)
	# 		c_type = mime.from_file(os.path.join(os.getcwd(), 'uploads', file))
	# 		msg.attach(file, c_type, fp.read())
	return msg