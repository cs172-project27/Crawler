import requests
import os
import json
import re

bearer_token = "AAAAAAAAAAAAAAAAAAAAAGImcQEAAAAAeVzfbOozV0ogH895rjehH3FT400%3DWI0VPPnC55EQ6fZRKiJOtpx8aIeZ5YbAkin85CNPfGeICWdkKi"

outfile = open('tweets.json', 'w')

def create_url():
    return "https://api.twitter.com/2/tweets/sample/stream?tweet.fields=created_at&expansions=author_id"


def bearer_oauth(r):
    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2SampledStreamPython"
    return r


def connect_to_endpoint(url):
    response = requests.request("GET", url, auth=bearer_oauth, stream=True)
    print(response.status_code)
    jsonIndex = 1
    for response_line in response.iter_lines():
        if response_line:
            tweetData = json.loads(response_line)

            text = tweetData['data']['text']
            urls = re.findall("http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", text)
            tweetData['urls'] = urls

            jsonString = json.dumps(tweetData, indent=4, sort_keys=True, ensure_ascii=False)
            jsonIndexString = str(jsonIndex)
            outfile.write('\"%s\": '%jsonIndexString)
            jsonIndex = jsonIndex + 1

            outfile.write(jsonString)

            outfile.write(',')
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )


def main():
    url = create_url()
    timeout = 0
    while True:
        connect_to_endpoint(url)
        timeout += 1


if __name__ == "__main__":
    main()