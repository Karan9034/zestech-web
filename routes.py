import os
from flask import Blueprint, render_template, url_for, redirect, request, flash
from form import QueryForm, send_mail

routes = Blueprint('routes', __name__)

@routes.route('/', methods=['GET','POST'])
def home():
	form = QueryForm()
	if form.submit.data:
		files = request.files.getlist("files")
		os.system('mkdir files')
		for file in files:
			file.save(os.path.join(os.getcwd(), 'files', file.filename))
		send_mail(form)
		os.system('rm -rf ./files')
		flash('We will reach out to you in a few days', 'success')
		return redirect(url_for('home'))
	return render_template('index.html', form=form)
