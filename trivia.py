def quiz(question, secret_word):
	guess = ""
	guess_count = 0
	guess_limit = 3
	out_of_guesses = False

	print(question)
	while guess != secret_word and not (out_of_guesses):
		if guess_count < guess_limit:
			guess = input("Enter guess: ")
			guess_count += 1
		else:
			out_of_guesses = True

	if out_of_guesses:
		print("Sorry you're out of guesses, you loose")
		print("The answer is",secret_word)
	else:
		print("Congrates, You win!")

def start_quiz():
	
	quiz("What animal has a long neck?", "giraffe")
	quiz("What color is the sky?","blue")
	quiz("British spy since the 60s","James Bond")

start_quiz()
print("End of Game")