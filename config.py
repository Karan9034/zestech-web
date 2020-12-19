import os

class Config():
    SECRET_KEY = ''
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = ''
    MAIL_PASSWORD = ''
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'files')