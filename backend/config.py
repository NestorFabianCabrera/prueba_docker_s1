import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'mysql+pymysql://user:password@db:3306/mydatabase'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
