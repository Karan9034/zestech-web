import os
from flask import Flask, render_template, url_for, redirect, request, flash
from form import QueryForm
from mail import send_mail
from flask_mail import Mail
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
mail = Mail(app)

@app.route('/', methods=['GET','POST'])
def home():
	form = QueryForm()
	if form.submit.data:
		files = request.files.getlist("files")
		os.system('mkdir uploads')
		for file in files:
			file.save(os.path.join(os.getcwd(), 'uploads', file.filename))
		# msg = send_mail(form)
		# mail.send(msg)
		# os.system('rm -rf ./uploads')
		flash('We will reach out to you in a few days', 'success')
		return redirect(url_for('home'))
	return render_template('index.html', form=form)



if __name__=="__main__":
	app.run(debug=True)