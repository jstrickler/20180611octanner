#!/usr/bin/env python
d1 = dict()
d2 = {'UT': 'Salt Lake City', 'NC': 'Raleigh'}
d3 = {}
d4 = dict(UT='Salt Lake City', NC='Raleigh')
st_caps = [
    ('UT','Salt Lake City'),
    ('NC', 'Raleigh'),
]
d5 = dict(st_caps)
print(d5)

states = ['UT', 'NC']
capitals = ['Salt Lake City', 'Raleigh']

state_capitals = dict(zip(states, capitals))
print(state_capitals)

state_capitals['OR'] = 'Salem'
state_capitals['CA'] = 'Sacramento'

print(state_capitals)
state_capitals['OR'] = 'Portland'
print(state_capitals)

print(state_capitals['NC'])

print(state_capitals.get('TX'))
print(state_capitals.get('TX', 'Nowheresville'))

print(state_capitals.setdefault('TX', 'Austin'))
print(state_capitals)

more_caps = {
    'SC': 'Columbia',
    'NC': 'Durham',
    'FL': 'Tallahassee',
    'MD': 'Annapolis',
}

state_capitals.update(more_caps)
