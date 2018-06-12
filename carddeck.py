#!/usr/bin/env python
# (c) John Strickler 2018
import random

class CardDeck():
    SUITS = 'Clubs Diamonds Hearts Spades'.split()
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

    def __init__(self, dealer):
        self.dealer = dealer
        self._make_deck()

    def _make_deck(self):
        self._cards = []
        for s in self.SUITS:
            for r in self.RANKS:
                card = f"{r}-{s}"
                self._cards.append(card)


    @property
    def cards(self):
        return self._cards


    def shuffle(self):
        random.shuffle(self._cards)

    def deal(self):
        return self._cards.pop()

    # def get_dealer(self):  #getter method (AKA accessor)
    #     return self._dealer
    #
    # def set_dealer(self, dealer): #setter (AKA mutator)
    #     self._dealer = dealer

    @property
    def dealer(self):  # getter property
        return self._dealer


    @dealer.setter
    def dealer(self, dealer): # setter property
        if isinstance(dealer, str):
            self._dealer = dealer
        else:
            raise TypeError("Dealer must be a string")

    def mymethod(self, file='config.txt', user='Bob'):
        pass

    @property
    def spam(self):
        return

    @spam.setter
    def spam(self, value):
        pass

    @property
    def ham(self):
        return

    @classmethod
    def get_suits(cls):
        return cls.SUITS

    def __len__(self):
        return len(self._cards)

    def __str__(self):
        my_type  = type(self)
        my_name = my_type.__name__
        return f"{my_name}({self.dealer},{len(self)})"

    def __add__(self, other):
        my_type = type(self) # get type of self
        tmp = my_type(self.dealer) # new instance of *type*
        tmp._cards = self.cards + other.cards
        return tmp
