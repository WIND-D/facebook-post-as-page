#!/usr/bin/env python

import requests, json, random
import facebook

#
# This script retrieves a random quote from random-quote-generator.herokuapp.com
# as a JSON object and posts the quote and author's name to Facebook
# By Arul John
# https://aruljohn.com
#

# Constants
app_id = '<<YOUR-APP_ID>>'
app_key = '<<YOUR-APP_KEY>>'
access_token = '<<YOUR-ACCESS_TOKEN>>'

# Functions
def random_quote():
    # GET request
    url = 'https://random-quote-generator.herokuapp.com/api/quotes/random'
    r = requests.get(url, timeout=10, headers = {'app_id': app_id, 'app_key': app_key})
    if r.status_code == 200:
        quote_json = r.json()
        quote = quote_json['quote'] + "\n ~ " + quote_json['author']
        return quote
    return 'ERROR: ' + str(r.status_code)

# Post to Facebook
try:
    graph = facebook.GraphAPI(access_token=access_token)
    graph.put_wall_post(message=random_quote())
except Exception as e:
    print 'Exception: ' + str(e)
    pass
