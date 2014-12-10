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
		if result == 'W':
			player_hand.bet_amount *= 2
		elif result == 'L':
			player_hand.bet_amount = 0
		results[result] = results[result] + 1
	print player_balance
	write_results()

def deal():
	global player_balance
	global player_hand
	global dealer_hand
	player_hand = Hand()
	dealer_hand = Hand()
	current_bet = 10
	player_hand.bet(current_bet)
	player_balance -= current_bet
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
	if dealer_exposed in ["2", "3", "4"]:
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
	global player_balance
	player_balance += player_hand.bet_amount
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
player_balance = 200

if __name__ == '__main__':
	main()
