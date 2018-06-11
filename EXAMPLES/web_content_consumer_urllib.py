#!/usr/bin/env python

import sys

import urllib.request, urllib.parse, urllib.error
import urllib.request, urllib.error, urllib.parse
import json

DATA_TYPE = 'application/json'

BASE_URL = 'http://lcboapi.com/products' # <1>
AUTH_TOKEN = 'CJAssociatesTraining'
AUTH_KEY= 'MDowYzMxMTg5Mi0yMzA5LTExZTUtODcxMC0wNzEwNDcxM2NkOTA6QVBxNklDQXU1M2RSNEkyUjBBOEpkZVNQQVJUYXY2Q3liSzBy'

def main(args):

    if len(args) < 1:
        print("Please specify a search term")
        sys.exit(1)

    search_term = args[0]

    setup_auth()

    params = make_params(search_term)

    url = BASE_URL + '?' + params # <2>

    do_query(url)


def do_query(url):
    response = urllib.request.urlopen(url) # <3>
    json_string = response.read().decode() # <4>
    
    raw_data = json.loads(json_string) # <5>
    # print('RAW JSON:', raw_data, '\n\n')
    if raw_data['result']:  # <6>
        for result in raw_data['result']:
            print("PRODUCT NUMBER:", result['product_no'])
            print("NAME:", result['name'])
            print("PACKAGE:", result['package'])
            print("PRICE: ${:5.2f}/liter".format(result['price_per_liter_in_cents']/100))
            print()
    else:
        print("Sorry, no items matched your query.")


def make_params(term):
    query_terms = { 'q': term }
    return urllib.parse.urlencode(query_terms) # <7>


def setup_auth():
    password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm() # <8>
    password_mgr.add_password(None, BASE_URL, AUTH_TOKEN, AUTH_KEY) # <9>
    auth_handler = urllib.request.HTTPBasicAuthHandler(password_mgr) # <10>
    opener = urllib.request.build_opener(auth_handler) # <11>
    urllib.request.install_opener(opener) # <12>


if __name__ == '__main__':
    main(sys.argv[1:])
