import os


# class Config:
#     SECRET_KEY = os.environ.get('SECRET_KEY')
#     SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
#     MAIL_SERVER = 'smtp.googlemail.com'
#     MAIL_PORT = 587
#     MAIL_USE_TLS = True
#     MAIL_USERNAME = os.environ.get('EMAIL_USER')
#     MAIL_PASSWORD = os.environ.get('EMAIL_PASS')



class Config:
    SECRET_KEY = 'wbljbljrgn3;krgv'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site1.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'newtonbuyukah@gmail.com'
    MAIL_PASSWORD = '0716434058'

