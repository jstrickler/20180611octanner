#!/usr/bin/env python
from pprint import pprint
import sys
import requests

BASE_URL = 'http://lcboapi.com/products'  # <1>
AUTH_TOKEN = 'CJAssociatesTraining' # <2>
AUTH_KEY= 'MDowYzMxMTg5Mi0yMzA5LTExZTUtODcxMC0wNzEwNDcxM2NkOTA6QVBxNklDQXU1M2RSNEkyUjBBOEpkZVNQQVJUYXY2Q3liSzBy'

def main(args):
    if len(args) < 1:
        print("Please specify a search term")
        sys.exit(1)
    
    response = requests.get(
        BASE_URL,
        params={ 'q': args[0] },
        auth=(AUTH_TOKEN, AUTH_KEY)
    ) # <3>

    if response.status_code == requests.codes.OK:
        # pprint(response.content)
        # print('-' * 60)
        raw_data = response.json() # <4>
        if raw_data['result']: # <5>
            for result in raw_data['result']:
                print("PRODUCT NUMBER:", result['product_no'])
                print("NAME:", result['name'])
                print("PACKAGE:", result['package'])
                print("PRICE: ${:5.2f}/liter".format(result['price_per_liter_in_cents']/100))
                print()
        else:
            print("Sorry, no items matched your query.")
    else:
        print("Sorry, HTTP response", response.status_code)
        
if __name__ == '__main__':
    main(sys.argv[1:])
