from flask import Flask, request, jsonify
from views import getDownloadLink, getVideoInfo
from db import db, db_url
from models import Videos

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = db_url
db.init_app(app)


@app.route("/")
def home():
    return "<p>Youtube to MP3 API</p>"

@app.route("/api/download", methods=["POST"])
def download_video():
    data = request.json
    link = data.get("link")

    if link:
        converter_data = getDownloadLink(link)
        youtube_data = getVideoInfo(link)

        video = Videos(
            id = converter_data['id'],
            title = youtube_data['title'],
            date = youtube_data['publish_date'],
            link = link,
            thumbnail_link = youtube_data['tb_link']
        )
        db.session.add(video)
        db.session.commit()

        return jsonify(
            {
                "id": converter_data['id'],
                "title": youtube_data['title'],
                "date": youtube_data['publish_date'],
                "link": link,
                "thumbnail_link": youtube_data['tb_link'],
                "download_link": converter_data
            }
        )
    
    else:
        return jsonify(
            {"message": "Please include a youtube link."}, 400
        )



if __name__ == '__main__':
    app.run(debug=True) 