import tweepy
from textblob import TextBlob

consumer_key = "lJ4VMzjQ1LjPJboT8BbJGZrH2"
consumer_secret = "tAgvoUe3Tz8i0fGfFf3nH8w8aJSmrbgyr1XLJ0avKYRf41NFwM"

access_token = "833179401474830338-pekqSC5eCwahbq3ZnB2LGOVejvyoEtY"
access_token_secret = "2xETXio4HIreXoVZFTw2IsNPvKJ4T673zUYEoox9SWlWz"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search("trump")

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)

