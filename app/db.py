import os
from dotenv import load_dotenv, find_dotenv
from flask_sqlalchemy import SQLAlchemy
load_dotenv(find_dotenv())

db = SQLAlchemy()
db_url = os.environ.get("DB_URL")