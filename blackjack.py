#!/usr/bin/env python
import random


def main():
	start_game()

def start_game():
	print "Welcome to Blackjack in Python!" 
	deck_count = raw_input('How many decks would you like to use? Enter #: ')
	deck_count = int(deck_count)
	print "The game will now start."

	shoe = Shoe(deck_count)
	shoe.merge_decks()
	shoe.shuffle_cards()

	player_hand = Hand()
	dealer_hand = Hand()
	
	player_hand.cards.append(shoe.cards.pop())
	dealer_hand.cards.append(shoe.cards.pop())
	print "Dealer shows %s" % (dealer_hand)
	player_hand.cards.append(shoe.cards.pop())
	dealer_hand.cards.append(shoe.cards.pop())


	print  'Your total value is %s' % (player_hand.calculate_value())

	while True:
		players_move = raw_input("Your hand is now %s. Would you like to hit or stand?" % (player_hand))
		if players_move == 'hit' or players_move == 'h':
			player_hand.cards.append(shoe.cards.pop())
			print  'Your total value is %s' % (player_hand.calculate_value())
		elif players_move == 'stand' or players_move == 's':
			print "Ok, you stand."
			break



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



class Shoe(object):
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
		random.shuffle(self.cards)

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
		ret = ''
		for card in self.cards:
			ret = ret + str(card) + ' '
		return ret

	def calculate_value(self):
		total = 0
		# turn total into the real total
		for card in self.cards:
			total = total + card_values[card_numbers.index(card.number)]
		has_ace = False
		for card in self.cards:
			if card.number == 'A':
				has_ace = True
		if total >= 11 and has_ace:
			total = total + 10 
		return total

card_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
card_numbers = ["A", '2', '3', '4', '5', '6', '7', '8', '9', '10', "J", "Q", "K"]
card_suits = ["H", "C", "D", "S"]
discard_pile = []
decks = []
master_deck = []

if __name__ == "__main__":	
	main()