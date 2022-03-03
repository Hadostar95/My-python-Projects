game_list= [0,1,2]
def display(game_list):
	print("Here is the current game list: ")
	print(game_list)

def replay():
	position_choice()
	replacement_choice(game_list,2)
	gameon()


def position_choice():

	choice = 'Wrong'

	ops=['0','1','2']

	while choice not in ops:

		choice = input("Pick a position (0,1,2): ")

		if choice not in ops:
			print("Sorry invalid choice")
			print(choice)
		else:
			print("aquate")
			print(choice)
def replacement_choice(game_list, position):
	user_placement = input("Type a string to place at position: ")
	game_list[position]= user_placement
	print(game_list)

def gameon():
	choice= 'Wrong'
	ans = ['Y','N']
	while choice not in ans:
		choice = input("Do You want to keep playing? Y = Yes, N = No ")
		if choice not in ans:
			print("Sorry, invalid anwser! Please choose Y or N")
	if choice == "Y":
		replay()
	else:
		
		print("Game list Updated:  ")
		for item in game_list:
			print(item)
		print("Thanks 4 playing")	






display(game_list)
position_choice()
replacement_choice(game_list,1)
gameon()
