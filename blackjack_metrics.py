#!/usr/bin/env python
from blackjack import Hand, Card, Deck
import gspread

#wks.update_acell('B2', "it's down there somewhere, let me take another look.")

def main():
	for i in range(100000):
		table_cleanup()
		deck.populate_deck()
		deck.shuffle_deck()
		deal()
		result = blackjack_check()
		if result == None:
			player_move()
			if player_hand.calculate_value() <= 21:
				dealer_move()
			result = comparison()
		#results.append(result)
		results[result] = results[result] + 1
	write_results()

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
	weak_dealer = False
	dealer_exposed = dealer_hand.cards[0].number
	if dealer_exposed in ["A", "2", "3", "4", "5", "6"]:
		weak_dealer = True
	while player_hand.calculate_value() <= 11 and weak_dealer == True:
		player_hand.cards.append(deck.cards.pop())


def dealer_move():
	while dealer_hand.calculate_value() <= 16:
		dealer_hand.cards.append(deck.cards.pop())
	if dealer_hand.calculate_value() <= 22:
		return "W"
	if dealer_hand.calculate_value() == player_hand.calculate_value:
		return "P"

def comparison():
	if player_hand.calculate_value() > 21:
		return "L"
	elif dealer_hand.calculate_value() > 21:
		return "W"
	elif player_hand.calculate_value() > dealer_hand.calculate_value():
		return "W"
	elif player_hand.calculate_value() == dealer_hand.calculate_value():
		return "P"
	elif player_hand.calculate_value() < dealer_hand.calculate_value():
		return "L"

def table_cleanup():
	player_hand.cards = []
	dealer_hand.cards = []
	deck.cards = []

def write_results():
	f = open('Blackjack Metrics.csv', 'w')
	for key in results:
		f.write(key)
		f.write(str(results[key]) + ' ')
	f.close()
	print results

results = {
	"P":0,
	"W":0,
	"L":0	
}

deck = Deck()
player_hand = Hand()
dealer_hand = Hand()

if __name__ == '__main__':
	main()
