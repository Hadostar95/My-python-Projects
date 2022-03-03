import random

def guessnuma():
	print('Welcome to guess that number')
	rannum = random.randrange(1,11)
	guess =''
	lst =[]
	while guess != rannum:
		guess = int(input('Input your guess: \n'))
		if guess == rannum:
			print(f'{rannum} is the correct number')
			for n in range(rannum):
				lst.append(n)
			popednum = lst.pop()	
		if guess > rannum:
			print('You overshot')
		if guess < rannum:
			print('too low')

	else:
		if popednum > 1:
			print(f'It took you {popednum} tries')
			print('thanks for playing')
		else:
			print(f'It took you 1 try nice')
			print('Thank you for playing')

def guessnumb():
	print('Welcome to guess that number part 2')
	rannum = random.randrange(1,11)
	guesscount=0
	guess = int(input('Enter your number:    '))
	while True:
		if guess == rannum:
			print('got it')
			print(f'took you {guesscount} guesses to guess right')
			break
			restart()
		if guess > rannum:
			print('overshot')
			guesscount += 1
			guess = int(input('Try again  \n'))
			#continue
		if guess < rannum:
			print('too low')
			guesscount += 1
			guess = int(input('Try again  \n'))
			#continue
	else:
		print('THANK YOU FOR PLAYING')
		print(f'took you {guesscount} guesses to guess right')
		restart()


def restart():
	ops =['y','n','Y','N']
	ans = ''

	print('Would you like to play again?',ops[0],'means yes while', ops[1],'means no')
	while ans not in ops:
		ans = input('Do you want to play again?: ')
		if ans in ops:
			if ans == ops[0] or ans == ops[2]:
				print('YESSSSSS')
				guessnuma()
				guessnumb()
			elif ans == ops[1] or ans == ops[3]:
				print('Exiting game')

		else:
			print('try again')
	else:
		print('Thank you')
guessnuma() 

guessnumb()

restart()