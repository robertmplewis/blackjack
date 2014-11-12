#!/usr/bin/env python
from blackjack import Hand, Card, Deck
import gspread

#wks.update_acell('B2', "it's down there somewhere, let me take another look.")

def main():
	deck.populate_deck()
	deck.shuffle_deck()
	deal()
	blackjack_check()

def deal():
	player_hand.cards.append(deck.cards.pop())
	dealer_hand.cards.append(deck.cards.pop())
	player_hand.cards.append(deck.cards.pop())
	dealer_hand.cards.append(deck.cards.pop())

def blackjack_check():
	if player_hand.blackjack_check() == True and dealer_hand.blackjack_check() == True:
		return 'P'
	elif player_hand.blackjack_check() == True and dealer_hand.blackjack_check() == False:
		return 'W'
	elif player_hand.blackjack_check() == False and dealer_hand.blackjack_check() == True:
		return 'L'
	return None

def player_move():
	if player_hand.calculate_value() >= 16 and dealer_under16 == True:
		player_hand.cards.append(deck.cards.pop())
def dealer_move():
	pass

def write_results():
	pass

results = []
deck = Deck()
player_hand = Hand()
dealer_hand = Hand()

if __name__ == '__main__':
	main()
