#!/usr/bin/env python
# (c) John Strickler 2018


class President():
    def __init__(self, term_number):
        with open('DATA/presidents.txt') as pres_in:
            for line in pres_in:
                term, *fields = line.rstrip().split(':')
                if term_number == int(term):
                    self._last_name = fields[0]
                    self._first_name = fields[1]
                    self._party = fields[-1]
                    break
            else:
                raise ValueError(f"No such president {term_number}")

    @property
    def last_name(self):
        return self._last_name

    @property
    def first_name(self):
        return self._first_name

    @property
    def party(self):
        return self._party

if __name__ == '__main__':

    p = President(26)
    print(p)
    print(p.first_name, p.last_name)

