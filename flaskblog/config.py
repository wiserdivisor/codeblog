import os

class Config:
    SECRET_KEY = os.environ.get('CODEBLOG_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('CODEBLOG_DB')
    MAIL_SERVER = os.environ.get('MAIL_GOOGLE')
    PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('FLOODWATCH_EMAIL')
    MAIL_PASSWORD = os.environ.get('FLOODWATCH_PSWRD')
