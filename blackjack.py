#!/usr/bin/env python
import random

def main():
	deck = Deck()
	deck.populate_deck()
	random.shuffle(deck.cards)
	players_hand = Hand()
	players_hand.cards.append(deck.cards.pop())
	players_hand.cards.append(deck.cards.pop())
	print players_hand.cards

class Deck(object):
	cards = []
	def populate_deck(self):
		for card_number in card_numbers:
			for card_suit in card_suits:
				card = Card(card_number, card_suit)
				self.cards.append(card)

class Card(object):
	def __init__(self, number, suit):
		self.number = number
		self.suit = suit
	def __repr__(self):
		return self.number + self.suit

class Hand(object):
	cards = []
	def __init__(self):
		pass


card_numbers = ["A", '2', '3', '4', '5', '6', '7', '8', '9', '10', "J", "Q", "K"]
card_suits = ["H", "C", "D", "S"]

	
if __name__ == "__main__":
	main()