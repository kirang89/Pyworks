#!/usr/bin/env python
#
# Tweet from command line
#

import twitter  # python-twitter
import sys

CONSUMER_KEY = 'consumer key'
CONSUMER_SECRET = 'consumer secret'
BASE_URL = 'https://api.twitter.com'
TOKEN = 'access token'
TOKEN_SECRET = 'access token secret'


def tweet(message):
    api = twitter.Api(consumer_key=CONSUMER_KEY,
                      consumer_secret=CONSUMER_SECRET,
                      access_token_key=TOKEN,
                      access_token_secret=TOKEN_SECRET)

    status = api.PostUpdate(message)
    print status

if __name__ == '__main__':
    message = sys.argv[1]
    if message:
        tweet(message)
    else:
        print "Enter something to tweet about"
