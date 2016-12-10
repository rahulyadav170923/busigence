import tweepy
import csv
from models import Tweets
from app import db

# initialise api instance
auth = tweepy.OAuthHandler('M39Nk7BorqtWj3jyHAhRnSNyd', 'Jjzw2WeWN8oDuevqhSMCYD629MVxMCBRhfo3mit08IHkMNEYIE')
auth.set_access_token('3130630774-mpgMGAyLTfQweuXqTw9Q9UHNQv5tHEbunXB6bnV', '0EhhSbA4DTGIz2zdT1N4zPAXgAPw7txYRWxzByP8A771o')
api = tweepy.API(auth)


def get_tweets_user(twitter_handle):
    tweets=api.search(q='@'+twitter_handle+' demonetisation',count=100)
    data=[i._json for i in tweets]
    return data

def tweets_in_csv(tweets):
    with open("tweets.csv",'wb') as out_file:
        csv_w = csv.writer(out_file)
        csv_w.writerow(['tweets'])
        for i in tweets:
            csv_w.writerow([i['text'].encode('utf-8')])

def tweets_in_sql(data,username):
    for i in data:
        tweets=Tweets()
        tweets.username=username
        tweets.tweet=i['text']
        db.session.add(tweets)
    db.session.commit()
