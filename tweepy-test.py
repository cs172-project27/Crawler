import tweepy
import urllib
import re

consumer_key = "pZ4SmVkzaw2Htna6gFHvCndDL"
consumer_secret = "kl3klUE5bY2R95A1bskmr6vYpL9pmRLpDBXzNtpE1dpXfVkbTO"

access_token = "1490394151791198209-UtEgfitS5KNQVFo1p2i8zapqty8weZ"
access_token_secret = "qQFdgLkyNH9L4j5wKmV56NxnID0vJgFT8yQnjHFJ2wwS0"

bearer_token = "AAAAAAAAAAAAAAAAAAAAAH5RcAEAAAAAV2jjHODhkoMhp9VuSBCoC1JdGeM%3DDFexcLWvkLLta81ZGny2f1tQpTyTOm10MDJtBt6dYD7Eontg2p"

tweets = []

class Tweet:
    def __init__(self, text, timestamp, geo, user, urls):
        self.text = text
        self.timestamp = timestamp
        self.geo = geo
        self.user = user
        self.urls = urls

class CustomStreamingClient(tweepy.StreamingClient):
    def on_tweet(self, tweet):
        urls = re.findall("http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", tweet.text)
        crawledTweet = Tweet(tweet.text, tweet.created_at, tweet.geo, tweet.author_id, urls)
        tweets.append(crawledTweet)
        print(tweet.data)

streaming_client = CustomStreamingClient(bearer_token)

streaming_client.sample()