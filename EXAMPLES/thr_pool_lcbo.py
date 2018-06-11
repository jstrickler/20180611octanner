#!/usr/bin/env python
from multiprocessing.dummy import Pool # <1>
from pprint import pprint
import requests

POOL_SIZE = 8
AUTH_TOKEN = 'CJAssociatesTraining' # <2>
AUTH_KEY= 'MDowYzMxMTg5Mi0yMzA5LTExZTUtODcxMC0wNzEwNDcxM2NkOTA6QVBxNklDQXU1M2RSNEkyUjBBOEpkZVNQQVJUYXY2Q3liSzBy'

BASE_URL = 'http://lcboapi.com/products'  # <3>

search_terms = [ # <4>
    'stolichnaya', 'makers mark', 'woodford', 'wombat', 'molson', 'moosehead',
    'michelob', 'bacardi', 'old rotgut', 'four roses', 'moonshine', 'harvest',
    'captain morgan', 'tanqueray','green spot', 'chartreuse'
]

def fetch_data(search_term):  # <5>
    response = requests.get(
        BASE_URL,
        auth=(AUTH_KEY, AUTH_TOKEN),
        params={ 'q': search_term },
    )   # <6>
    raw_json = response.json() # <7>
    names = []
    if raw_json['result']:
        for result in raw_json['result']:
            names.append(result['name'])
    return names  # <8>

p = Pool(POOL_SIZE)  # <9>

results = p.map(fetch_data, search_terms)  # <10>

for search_term, result in zip(search_terms, results):  # <11>
    print("{}:".format(search_term.upper()))
    if result:
        pprint(result)
    else:
        print("** no results **")
