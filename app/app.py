from flask import Flask, request, jsonify
from views import getDownloadLink, getVideoInfo, getDownloadStatus
from db import db, db_url
from models import Videos
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = db_url
db.init_app(app)

@app.route("/")
def home():
    return "<p>Youtube to MP3 API</p>"


@app.route("/api", methods=["GET"])
def get_videos():
    video_objects = Videos.query.filter_by().all()
    videos = []
    
    for video in video_objects:
        videos.append({
            "id": video.id,
            "title": video.title,
            "date": video.date,
            "link": video.link,
            "thumbnail_link": video.thumbnail_link
        })

    return jsonify(videos, 200)


@app.route("/api/download", methods=["POST"])
def download_video():
    data = request.json
    link = data['link']

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
                "download_link": converter_data['download_url'],
                "status": "CONVERTING"
            }, 201
        )
    
    else:
        return jsonify(
            {"message": "Please include a youtube link."}, 400
        )

@app.route("/api/download/<id>", methods=["GET"])
def get_status(id):
    status = getDownloadStatus(id)

    return jsonify(status, 200)


@app.route("/api/download/<id>", methods=["DELETE"])
def delete_video(id):
    video = Videos.query.get(id)

    db.session.delete(video)
    db.session.commit()

    return jsonify({"message": "Video successfully deleted"}, 200)


if __name__ == '__main__':
    app.run(debug=True) 