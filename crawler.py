import requests
import os
import json
import re
from bs4 import BeautifulSoup
import validators
import sys

file_name = 'tweets.json'
bearer_token = "AAAAAAAAAAAAAAAAAAAAAGImcQEAAAAAeVzfbOozV0ogH895rjehH3FT400%3DWI0VPPnC55EQ6fZRKiJOtpx8aIeZ5YbAkin85CNPfGeICWdkKi"
outfile = open(file_name, 'w')
max_index = 2000000

def create_url():
    return "https://api.twitter.com/2/tweets/sample/stream?tweet.fields=created_at&expansions=author_id"


def bearer_oauth(r):
    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2SampledStreamPython"
    return r


def connect_to_endpoint(url):
    response = requests.request("GET", url, auth=bearer_oauth, stream=True)
    print(response.status_code)
    json_index = 1
    for response_line in response.iter_lines():
        if response_line:
            tweetData = json.loads(response_line)

            text = tweetData['data']['text']
            urls = re.findall("http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", text)
            tweetData['urls'] = urls

            for url in urls:
                if validators.url(url):
                    try:
                        reqs = requests.get(url, timeout=10)
                        soup = BeautifulSoup(reqs.text, 'html.parser')
                        titles = []
                        for title in soup.find_all('title'):
                            titles.append(title.get_text())
                            break
                        tweetData['titles'] = titles
                    except:
                        print("Unable to fetch page title")

            json_string = json.dumps(tweetData, indent=4, sort_keys=True, ensure_ascii=False)
            json_index_string = str(json_index)
            outfile.write('\"%s\": '%json_index_string)

            json_index = json_index + 1
            if json_index >= max_index:
                break

            outfile.write(json_string)
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
    custom_name = str(sys.argv[1])   
    if (custom_name.endswith('.json')):
        file_name = custom_name

    custom_length = sys.argv[2]
    if custom_length.isdigit():
        max_index = custom_length

    main()