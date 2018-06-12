#!/usr/bin/env python
# (c) John Strickler 2018

from carddeck import CardDeck
from jokerdeck import JokerDeck

# CardDeck d1 = new CardDeck(..)
d1 = CardDeck('Victor')
d2 = CardDeck('Camilla')

print(d1, d2)
# print(d1.get_dealer())
# print(d2.get_dealer())
#
# d1.set_dealer('Roderick')
# print(d1.get_dealer())

print(d1.dealer)

d1.dealer = 'Charles'
print(d1.dealer)
d1.shuffle()
print(d1.cards, '\n')

hand = []

for i in range(5):
    hand.append(d1.deal())

print(hand, '\n')

print(d1.get_suits(), '\n')

print(CardDeck.get_suits())

j1 = JokerDeck("Alberta")
print(j1.dealer)
j1.shuffle()
print(j1.cards, '\n')
print(j1)
print(d1)
print(len(d1), len(j1))

new_deck = d1 + j1

print(new_deck)
print(new_deck.cards)
