#!/usr/bin/env python
# (c) John Strickler 2018

from carddeck import CardDeck

class JokerDeck(CardDeck):
    def _make_deck(self):
        super()._make_deck()
        self._cards.append('Red-Joker')
        self._cards.append('Black-Joker')
