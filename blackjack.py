#!/usr/bin/env python
import random

def main():
	start_game()

def start_game():
	print "Welcome to Blackjack in Python!" 
	deck_count = raw_input('How many decks would you like to use? Enter 1-6: ')
	deck_count = int(deck_count)
	if deck_count > 6:
		print 'Too many decks selected.'
		return

	for i in range(deck_count):
		deck = Deck()
		deck.populate_deck()
		decks.append(deck)
	
	
	for deck in decks:
		master_deck.extend(deck.cards)
	random.shuffle(master_deck)

	
			
	players_hand = Hand()
	players_hand.cards.append(master_deck.pop())
	players_hand.cards.append(master_deck.pop())
	print players_hand.cards

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

class Card(object):
	def __init__(self, number, suit):
		self.number = number
		self.suit = suit

	def __repr__(self):
		return self.number + self.suit

class Hand(object):
	def __init__(self):
		self.cards = []


card_numbers = ["A", '2', '3', '4', '5', '6', '7', '8', '9', '10', "J", "Q", "K"]
card_suits = ["H", "C", "D", "S"]
discard_pile = []
decks = []
master_deck = []

if __name__ == "__main__":	
	main()