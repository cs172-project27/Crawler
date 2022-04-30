import tweepy

bearer_token = "AAAAAAAAAAAAAAAAAAAAAGwqcAEAAAAAew5fSszXMJz4npuFgAeE7RVpUCo%3D8EB29IRC2vMKQxNOlL5hhJmlziqxMcl5hNPMPaCCGFIe7dZGRz"

class CustomStreamingClient(tweepy.StreamingClient):
    def on_tweet(self, tweet):
        print(tweet.data)

streaming_client = CustomStreamingClient(bearer_token)

streaming_client.add_rules(tweepy.StreamRule("iPhone 13"))
streaming_client.filter()
