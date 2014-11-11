#!/usr/bin/env python
import random

def main():
	start_game()
	test_blackjack()

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
	blackjack = []
	
	player_hand.cards.append(shoe.cards.pop())
	dealer_hand.cards.append(shoe.cards.pop())
	print "Dealer shows %s" % (dealer_hand)
	player_hand.cards.append(shoe.cards.pop())
	dealer_hand.cards.append(shoe.cards.pop())

	if player_hand.blackjack_check == True and dealer_hand.blackjack_check == True:
		print "Push! Player and dealer have blackjack"
	elif player_hand.blackjack_check == True and dealer_hand.blackjack_check == False:
		print "Your hand is a blackjack! You win!"
	elif player_hand.blackjack_check == False and dealer_hand.blackjack_check == True:
		print "Dealer has blackjack. You lose."


	print  'Your total value is %s' % (player_hand.calculate_value())

	while True:
		players_move = raw_input("Your hand is now %s. Would you like to hit or stand?" % (player_hand))
		if players_move == 'hit' or players_move == 'h':
			player_hand.cards.append(shoe.cards.pop())
			print  'Your total value is %s' % (player_hand.calculate_value())
		elif players_move == 'stand' or players_move == 's':
			print "Ok, you stand at %s" % (player_hand.calculate_value())
			break

def game_outcome(player_hand, dealer_hand):
	discard_pile = player_hand.pop() and dealer_hand.pop()
	if player_hand.calculate_value < 21 and dealer_hand.calculate_value < player_hand.calculate_value:
		print "Congratulations you've won!"
	if player_hand.calculate_value > 21:
		print "Bust! You lose."





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

	def has_ace(self):
		ret = False
		for card in self.cards:
			if card.number == 'A':
				ret = True
		return ret

	def blackjack_check(self):
		if self.has_ace() == True and len(self.cards) == 2 and self.calculate_value() == 21:
			return True
		return False

	def calculate_value(self):
		total = 0
		# turn total into the real total
		for card in self.cards:
			total = total + card_values[card_numbers.index(card.number)]
		if total >= 11 and self.has_ace():
			total = total + 10 
		return total

card_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
card_numbers = ["A", '2', '3', '4', '5', '6', '7', '8', '9', '10', "J", "Q", "K"]
card_suits = ["H", "C", "D", "S"]
discard_pile = []
decks = []
master_deck = []

''' ******************************
                TESTS
    ****************************** '''
def test_blackjack():
	hand = Hand()
	card1 = Card("9", "H")
	card2 = Card("A", "H")
	hand.cards.append(card1)
	hand.cards.append(card2)
	print hand
	print hand.blackjack_check()

if __name__ == "__main__":	
	main()