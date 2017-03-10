# Using yelp api to generat poem <Today's never ending eating story>
# https://www.yelp.com/developers/documentation/v2/search_api
#For Reading and Writing Electronic Text in ITP NYU SPRING 2017, taught by Allison Parrish
#Yuli Cai Mar 9 2017

import requests
import oauth2
import sys
import json
import urllib
import random
import io

term_param = sys.argv[1]
location_param = sys.argv[2]
# 0=Best matched (default), 1=Distance, 2=Highest Rated.
# If the mode is 1 or 2 a search may retrieve an additional 20 businesses past the initial limit of the first 20 results.
# This is done by specifying an offset and limit of 20.
base_url = 'http://api.yelp.com/v2/search?sort=2'
# params = urllib.urlencode{'term'}
search_term = dict(term=term_param,location=location_param)
# search_url = urllib.urlencode(search_term)


with io.open('cred.json') as cred:
    creds = json.load(cred)


def request(url, url_params=None):
    consumer_key = creds['consumer_key']
    consumer_secret = creds['consumer_secret']
    token = creds['token']
    token_secret =creds['token_secret']

    url_params = url_params or {}
    consumer = oauth2.Consumer(consumer_key, consumer_secret)
    oauth_request = oauth2.Request(method="GET", url=url, parameters=url_params)

    oauth_request.update(
        {
            'oauth_nonce': oauth2.generate_nonce(),
            'oauth_timestamp': oauth2.generate_timestamp(),
            'oauth_token': token,
            'oauth_consumer_key': consumer_key
        }
    )
    token = oauth2.Token(token, token_secret)
    oauth_request.sign_request(oauth2.SignatureMethod_HMAC_SHA1(), consumer, token)
    signed_url = oauth_request.to_url()
    raw = urllib.urlopen(signed_url).read()
    data=json.loads(raw)
    return data
    # return requests.get(signed_url).json()
response = request(base_url,url_params=search_term)

categories=[]
streets=[]
texts = []
for business in response['businesses']:
    defaut_street = 'broadway & waverly pl'
    # If you don't want to have an exception but would rather a default value used instead, you can use the get() method:
    streets.append(business['location'].get("cross_streets",defaut_street))
    for category in business['categories']:
        categories.append(category[0])
    texts.append(business['snippet_text'])

print 'Today, at '+random.choice(streets)
print 'I had a ' +random.choice(categories)+" "+ term_param
print random.choice(texts)
print '\n'
print '>>>>>>>>>>>>>>>'
