from flask import Flask,jsonify
import json
import os
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

package_dir = os.path.abspath(os.path.dirname(__file__))
database_path = os.path.join(package_dir, 'test.db')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+database_path
db = SQLAlchemy(app)
db.drop_all()
db.create_all()
from twitter import get_tweets_user,tweets_in_csv,tweets_in_sql



# twitter views

@app.route("/get_tweets/<username>")
def get_tweets(username):
    data=get_tweets_user(username)
    tweets_in_csv(data)
    #tweets_in_sql(data,username)
    return jsonify(data)



# csv views
