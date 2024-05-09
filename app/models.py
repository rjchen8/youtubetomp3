from db import db
class Videos(db.Model):
    __tablename__ = "Videos"
    id = db.Column(db.String(255), primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    link = db.Column(db.String(255), nullable=False)
    thumbnail_link = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f'<Video {self.title} {self.id}'