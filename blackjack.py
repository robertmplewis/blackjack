#!/usr/bin/env python

def main():
	deck = Deck()
	deck.populate_deck()
	print deck.cards

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

card_numbers = ["A", '2', '3', '4', '5', '6', '7', '8', '9', '10', "J", "Q", "K"]
card_suits = ["H", "C", "D", "S"]
	
if __name__ == "__main__":
	main()