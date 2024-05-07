from app import db

class Videos(db.Model):
    __tablename__ = "Videos"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    thumbnail = db.Column(db.String(255), nullable=False)
    length = db.column(db.Integer, nullable=False)
    author = db.column(db.String(255), nullable=False)
    date = db.column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'<Video {self.title} {self.id}'