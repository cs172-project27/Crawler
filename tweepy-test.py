import tweepy
import urllib
import re

tweets = []
bearer_token = "AAAAAAAAAAAAAAAAAAAAAGwqcAEAAAAAew5fSszXMJz4npuFgAeE7RVpUCo%3D8EB29IRC2vMKQxNOlL5hhJmlziqxMcl5hNPMPaCCGFIe7dZGRz"

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
        tweets.append(crawled_tweet)

streaming_client = CustomStreamingClient(bearer_token)

filterRules = streaming_client.get_rules()[0]
if filterRules is not None:
    rules_to_delete = []
    for rule in filterRules:
        rules_to_delete.append(rule.id)
    streaming_client.delete_rules(rules_to_delete)

streaming_client.add_rules(tweepy.StreamRule("Elon Musk"))
streaming_client.filter()
