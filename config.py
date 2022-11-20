import os
from dotenv import load_dotenv

load_dotenv()

class Config:
	"""Set Flask config variables."""

	FLASK_ENV = 'development'
	TESTING = True
	DEBUG = True
	SECRET_KEY = os.environ.get('SECRET_KEY')
	SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
	