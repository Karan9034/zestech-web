import os
from app import app
from flask import render_template, url_for, redirect, request, flash
from form import QueryForm, send_mail

@app.route('/', methods=['GET','POST'])
def home():
	form = QueryForm()
	if form.submit.data:
		files = request.files.getlist("files")
		os.system('mkdir files')
		for file in files:
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
		send_mail(form)
		os.system('rm -rf ./files')
		flash('We will reach out to you in a few days', 'success')
		return redirect(url_for('home'))
	return render_template('index.html', form=form)
