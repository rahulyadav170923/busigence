from app import db

class Tweets(db.Model):
    __tablename__='Tweets'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    tweet = db.Column(db.String(120))
