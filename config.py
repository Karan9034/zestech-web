import os

class Config():
    SECRET_KEY = 'c9baac77-7603-488e-a2a0-36759b44f0c0'
    # EMAIL_USER= ''
    # EMAIL_PASSWORD= ''
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'files')