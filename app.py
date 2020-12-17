import os
from flask import Flask, render_template, url_for, redirect, request, flash
from form import QueryForm, send_mail
from config import Config
# from flask_mail import 

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/', methods=['GET','POST'])
def home():
	form = QueryForm()
	if form.submit.data:
		files = request.files.getlist("files")
		os.system('mkdir files')
		for file in files:
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
		send_mail()
		os.system('rm -rf ./files')
		os.system('del /F/Q/S .\\files')
		flash('We will reach out to you in a few days', 'success')
		return redirect(url_for('home'))
	return render_template('index.html', form=form)

if __name__=="__main__":
	app.run(debug=True)