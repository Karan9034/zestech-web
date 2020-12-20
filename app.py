import os, magic
from flask import Flask, render_template, url_for, redirect, request, flash
from form import QueryForm
from flask_mail import Mail, Message
from werkzeug.utils import secure_filename
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
mail = Mail(app)

encoding_guess_list=['utf8', "cp1252" ,'latin1']


def send_mail(form):
	msg = Message("Quote Enquiry Mail", sender='mindblogger@hotmail.com', recipients=['karan.agr9034@gmail.com'])
	msg.body = f'''Email: {form.email.data}
Phone: {form.phone.data}
Address: {form.address.data}
Average Monthly Bill: {form.bill.data}
Message: {form.message.data}
'''
	for file in os.listdir(os.path.join(os.getcwd(), 'files')):
		for encoding in encoding_guess_list:
			try:
				fp = open(os.path.join(os.getcwd(), 'files', file), 'rt', encoding=encoding)
				mime = magic.Magic(mime=True)
				c_type = mime.from_file(os.path.join(os.getcwd(), 'files', file))
				msg.attach(file, c_type, fp.read())
				fp.close()
			except:
				continue
	mail.send(msg)

@app.route('/', methods=['GET','POST'])
def home():
	form = QueryForm()
	if form.submit.data:
		upfile = request.files['files']
		os.system('mkdir ./files')
		upfile.save(os.path.join(os.getcwd(), 'files', secure_filename(upfile.filename)))
		send_mail(form)
		os.system('rm -r ./files/*')
		flash('We will reach out to you in a few days', 'success')
		return redirect(url_for('home'))
	return render_template('index.html', form=form)



if __name__=="__main__":
	app.run(debug=True)