from flask import Flask
from flask_mail import Mail
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
mail = Mail(app)


if __name__=="__main__":
	app.run(debug=True)