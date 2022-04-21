import os
import django_heroku

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = "sqlite:///site.db"

DEBUG_VALUE = True
ALLOWED_HOSTS = ["did-you.herokuapp.com"]

django_heroku.settings(locals())