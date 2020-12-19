from flask import Flask
from flask_mail import Mail
from config import Config
from routes import routes

app = Flask(__name__)
app.config.from_object(Config)
mail = Mail(app)
app.register_blueprint(routes)

if __name__=="__main__":
	app.run(debug=True)