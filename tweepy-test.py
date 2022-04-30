import tweepy
import json

bearer_token = "AAAAAAAAAAAAAAAAAAAAAGwqcAEAAAAAew5fSszXMJz4npuFgAeE7RVpUCo%3D8EB29IRC2vMKQxNOlL5hhJmlziqxMcl5hNPMPaCCGFIe7dZGRz"

class CustomStreamingClient(tweepy.StreamingClient):
    def on_tweet(self, tweet):
        print(tweet.data)

streaming_client = CustomStreamingClient(bearer_token)


filterRules = streaming_client.get_rules()[0]
if filterRules is not None:
    rules_to_delete = []
    for rule in filterRules:
        rules_to_delete.append(rule.id)
    streaming_client.delete_rules(rules_to_delete)

streaming_client.add_rules(tweepy.StreamRule("#DoctorStrange"))
streaming_client.filter()
