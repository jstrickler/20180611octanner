#!/usr/bin/env python
john_countries = """Canada
Mexico
Barbados
China
UK
Austria
Spain
Bulgaria
Israel""".split()

clare_countries = """British Virgin Islands
Denmark
UK
Spain
Kenya
Mexico
Barbados
Norway
Sweden
Canada""".split('\n')

john = set(john_countries)
clare = set(clare_countries)

print("both:", john & clare)
print("all:", john | clare)
print("just one:", john ^ clare)
print("just John:", john - clare)
print("just Clare:", clare - john)
