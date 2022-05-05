import tweepy
import urllib
import re

consumer_key = "BSnHHnsiKTiFdx7my3AOShGD6"
consumer_secret = "COm3WakQurOycapsZucd8VEGCoZ7bwlmGViWQMvrlSID0N2y6m"

access_token = "1490394151791198209-SECeYJWboasBDTvWbbDugPDiYLR0UW"
access_token_secret = "9EHjVUhlTCHA8bbhUY1VFu6ELKRopPfD9sQCzX3vEiVL5"

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

filterRules = streaming_client.get_rules()[0]
if filterRules is not None:
    rules_to_delete = []
    for rule in filterRules:
        rules_to_delete.append(rule.id)
    streaming_client.delete_rules(rules_to_delete)

streaming_client.add_rules(tweepy.StreamRule("Elon Musk"))
streaming_client.filter()