import random

suits = ('Hearts', 'Dimonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

values = {'Two':2 , 'Three':3 , 'Four':4 , 'Five':5 ,'Six':6 ,'Seven':7 , 'Eight':8 ,
	'Nine':9 ,'Ten':10 ,'Jack':11 , 'Queen':12 ,'King':13 , 'Ace':14}

class Card:
	def __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank
		self.value = values[rank]

	def __str__(self):
		return self.rank + " of " + self.suit

#	def 

tow_hearts = Card("Spades","Two")
print(tow_hearts)
print(tow_hearts.suit)
print(tow_hearts.rank)
three_clubs = Card("Clubs","Three")
print(three_clubs.value)


print(values[tow_hearts.rank])

if tow_hearts.value < three_clubs.value:
	print('Hello')
		
else:
	print('Greater')

for i in suits:
	print(i)

for j in values:
	print(values[j])


