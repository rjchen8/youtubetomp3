import os
from flask import Flask, request, make_response
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

app = Flask(__name__)
db = SQLAlchemy()

db_url = os.environ.get("DB_URL")
app.config["SQLALCHEMY_DATABASE_URI"] = db_url

db.init_app(app)


@app.route("/")
def home():
    return "<p>Youtube to MP3 API</p>"

@app.route("/api/download", methods=["POST"])
def download():
    data = request.json
    link = data.get("link")
    
    if link:
        return make_response(
            {"message": "Add logic here"},
            201
        )

if __name__ == '__main__':
    app.run(debug=True) 