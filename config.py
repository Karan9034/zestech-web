import os

class Config():
    SECRET_KEY = 'c9baac77-7603-488e-a2a0-36759b44f0c0'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'inquiry.zestech@gmail.com'
    MAIL_PASSWORD = '1234Abcd9@'
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'files')