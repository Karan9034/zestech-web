import os, magic
from flask import Flask, render_template, url_for, redirect, request, flash
from form import QueryForm
from flask_mail import Mail, Message
from werkzeug.utils import secure_filename
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
mail = Mail(app)

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
	mail.send(msg)

@app.route('/', methods=['GET','POST'])
def home():
	form = QueryForm()
	if form.submit.data:
		files = request.files['files']
		os.system('mkdir ./files')
		for file in files:
			file.save(os.path.join(os.getcwd(), 'files', secure_filename(file.filename)))
		send_mail(form)
		os.system('rm -r ./files/*')
		flash('We will reach out to you in a few days', 'success')
		return redirect(url_for('home'))
	return render_template('index.html', form=form)



if __name__=="__main__":
	app.run(debug=True)