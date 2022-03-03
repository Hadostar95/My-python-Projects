import random

suits = ('Hearts', 'Dimonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

values = {'Two':2 , 'Three':3 , 'Four':4 , 'Five':5 ,'Six':6 ,'Seven':7 , 'Eight':8 ,
	'Nine':9 ,'Ten':10 ,'Jack':11 , 'Queen':12 ,'King':13 , 'Ace':14}

playing = True

class Card:
	def __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank
		#self.value = values[rank]

	def __str__(self):
		return self.rank + " of " + self.suit

class Deck:
	"""docstring for Deck"""
	def __init__(self):
		self.deck = []
		for suit in suits:
			for rank in ranks:
				self.deck.append(Card(suit,rank))

	def __str__(self):
		deck_comp = ''
		for card in self.deck:
			deck_comp += '\n'+ card.__str__()
		return 'The deck has:  '+ deck_comp

	def shuffle(self):
		random.shuffle(self.deck)

	def deal(self):
		single_card = self.deck.pop()
		return single_card




class  Hand:
	"""docstring for  Hand"""
	def __init__(self):
		self.cards = []
		self.value = 0
		self.aces = 0

	def add_card(self,card):
		self.cards.append(card)
		self.value += values[card.rank]

		if card.rank == 'Ace':
			self.aces += 1

	def adjust_for_ace(self):
		#IF TOTAL VALUE > 21 AND STILL HAVE AN ACE
		#THAN CHANGE MY ACE TO B A 1 INSTEAD OF 11
		while self.value > 21 and self.aces:
			self.value -= 10
			self.aces -= 1
class Chips:
	"""docstring for Chips"""
	def __init__(self):
		self.total = 100
		self.bet = 0

	def win_bet(self):
		self.total += self.bet

	def lose_bet(self):
		self.total -= self.bet
		

def take_bet(chips):
	while True:

		try:
			chips.bet = int(input('How many chips would you like to bet? \n'))
		except ValueError:
			print('sorry please provide a number/Interger')
		else:
			if chips.bet > chips.total:
				print(f'Sorry you do not have enough chips! \n You have:  {chips.total}')
			else:
				break

def hit(deck,hand):
	single_card = deck.deal()
	hand.add_card(single_card)
	hand.adjust_for_ace()

def hit_or_stand(deck, hand):
	global playing

	while  True:

		x = input('Hit or stand? Enter h or s \n')
			
		if x[0].lower() == 'h' or x[0].upper() == 'H':
			hit(deck,hand)

		elif x[0].lower() == 's' or x[0].upper() == 'S':
			print("Player stands... Dealer's turn")
			playing = False

		else:
			print("Sorry I did not understand that, please enter: s or h only")
			continue
		break
def player_busts(player,dealer,chips):
	print("Bust player")
	chips.lose_bet()


def player_wins(player,dealer,chips):
	print("Player wins")
	chips.win_bet()

def dealer_busts(player,dealer,chips):
	print("Player wins! Bust Dealer")
	chips.win_bet()

def dealer_wins(player,dealer,chips):
	print("Dealer wins")
	chips.lose_bet()

def push(player,dealer):
	print("Dealer and Player tie! PUSH")

#def show_some(player, dealer):
#	print("Dealer's hand:")
#	print('one card hidden!')
#	print('', dealer.cards[1])
#	print('\n')
#	print("Player's Hand:")
#	for card in player.cards:
#		print(card)

#def show_all(player,dealer):
#	print("Dealer's Hand:")
#	for card in dealer.cards:
#		print(card)
#	print('\n')
#	print("Player's hand: ")
#	for card in player.cards:
#		print(card)

def show_some(player,dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('',dealer.cards[1])  
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    
def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)
		
#Deck testing
test_deck = Deck()
test_deck.shuffle()
#List of cards
#print(test_deck)
#Player
test_player = Hand()
pulled_card = test_deck.deal()
print(f'Your Pulled card is the: {pulled_card}')
print('')
test_player.add_card(pulled_card)
print(f'Value is: {test_player.value}')
print('')
print('adding to value')
#test_player.add_card(test_deck.deck.deal())
#print(test_player.value)
	
		
while True:
	#Print opening statement
	print('***************************Welcome to Black Jack******************************')

	#Create and shuffle deck
	deck = Deck()
	deck.shuffle()

	
	player_hand = Hand()
	player_hand.add_card(deck.deal())
	player_hand.add_card(deck.deal())

	dealer_hand = Hand()
	dealer_hand.add_card(deck.deal())
	dealer_hand.add_card(deck.deal())



	#set up player chips
	player_chips = Chips()


	#prompt the player for their bet
	take_bet(player_chips)

	#show cards (but keep the dealer's cards hidden)
	show_some(player_hand,dealer_hand)

	while playing: # recall varible from hit or stand func
		#prompt for player to hit or stand
		hit_or_stand(deck, player_hand)


		#show cards (but the dealers's)
		show_some(player_hand,dealer_hand)

		#If player's hand exeeds 21 run player_bust func and break out of loop
		if player_hand.value > 21:
			player_busts(player_hand,dealer_hand, player_chips)
			break



	#If player hasn't busted, play Dealer's hand until Dealer reachs 17
	if player_hand.value <= 21:
		while  dealer_hand.value < player_hand.value:
			hit(deck, dealer_hand)


		#Show all cards
		show_all(player_hand, dealer_hand)

		#run different winning scenarios
		if dealer_hand.value > 21:
			dealer_busts(player_hand,dealer_hand,player_chips)
		elif dealer_hand.value > player_hand.value:
			dealer_wins(player_hand, dealer_hand, player_chips)
		elif dealer_hand.value < player_hand.value:
			player_wins(player_hand,dealer_hand,player_chips)
		else:
			push(player_hand, dealer_hand)



	#Inform player of their chips total
	print(f"\n Player's total chips are at:   {player_chips.total}")


	#Ask to play again
	new_game = input('Would you like to play again? y/n:   ')
	if new_game[0].lower() == 'y' or new_game[0].upper()=='Y':
		playing = True


	elif new_game[0].lower() == 'n' or new_game[0].upper() == 'N':
		print('Thank you for playing!')
		break






	#