import os
from flask import Flask
from sqlalchemy import create_engine
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
db_url = os.environ.get("DB_URL")

app = Flask(__name__)
engine = create_engine(db_url, echo=True)

@app.route("/")
def hello_world():
    return "<p>hello bro</p>"

if __name__ == '__main__':
    app.run(debug=True) 