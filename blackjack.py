#!/usr/bin/env python
import random

def main():
	start_game()

def start_game():
	print "Welcome to Blackjack in Python!" 
	deck_count = raw_input('How many decks would you like to use? Enter #: ')
	deck_count = int(deck_count)
	print "The game will now start."

	deck_collection = DeckCollection(deck_count)
	deck_collection.merge_decks()

	player_hand = Hand()
	dealer_hand = Hand()
	
	player_hand.cards.append(deck_collection.cards.pop())
	dealer_hand.cards.append(deck_collection.cards.pop())
	print "Dealer shows %s" % (dealer_hand)
	player_hand.cards.append(deck_collection.cards.pop())
	dealer_hand.cards.append(deck_collection.cards.pop())

	raw_input("Your hand is now %s. Would you like to hit or stand?" % (player_hand))




class Deck(object):
	def __init__(self):
		self.cards = []

	def __repr__(self):
		return "This deck has %s cards." % len(self.cards)

	def populate_deck(self):
		for card_number in card_numbers:
			for card_suit in card_suits:
				card = Card(card_number, card_suit)
				self.cards.append(card)

	def shuffle_deck(self):
		random.shuffle(self.cards)
		print "The deck has now been shuffled!"

class DeckCollection(object):
	def __init__(self, deck_count):
		self.decks = []
		self.cards = []
		for i in range(deck_count):
			deck = Deck()
			deck.populate_deck()
			self.decks.append(deck)


	def merge_decks(self):
		for deck in self.decks:
			self.cards.extend(deck.cards)
		self.decks = []

	def shuffle_cards(self):
		random.shuffle(deck.cards)

	def __repr__(self):
		return "A collection of %s decks." % (len(self.decks))


class Card(object):
	def __init__(self, number, suit):
		self.number = number
		self.suit = suit

	def __repr__(self):
		return self.number + self.suit

class Hand(object):
	def __init__(self):
		self.cards = []

	def __repr__(self):
		if len(self.cards) == 1:
			return str(self.cards[0])
		else:
			return "%s, %s" % (str(self.cards[0]), str(self.cards[1])) 
		

card_numbers = ["A", '2', '3', '4', '5', '6', '7', '8', '9', '10', "J", "Q", "K"]
card_suits = ["H", "C", "D", "S"]
discard_pile = []
decks = []
master_deck = []

if __name__ == "__main__":	
	main()