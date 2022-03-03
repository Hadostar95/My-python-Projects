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
		self.value = values[rank]

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




class  Hand():
	"""docstring for  Hand"""
	def __init__(self):
		self.cards = []
		self.value = 0
		self.aces = 0

	def add_card(self, card):

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

		
#Deck testing
test_deck = Deck()
test_deck.shuffle()
print(test_deck)
#Player
test_player = Hand()
pulled_card = test_deck.deal()
print('Pulled card: ')
print(pulled_card)
test_player.add_card(pulled_card)
print('Value')
print(test_player.value)
print('adding to value')
#test_player.add_card(test_deck.deck.deal())
#print(test_player.value)
	
		
