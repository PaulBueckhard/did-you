class Config:
    SECRET_KEY = "42c9e524660fa3d7921cb42d37c0643e"
    SQLALCHEMY_DATABASE_URI = "sqlite:///site.db".replace('postgres://', 'postgresql://', 1)

ALLOWED_HOSTS = ["did-you.herokuapp.com"]