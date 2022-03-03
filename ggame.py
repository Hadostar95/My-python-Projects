print("Hi there");
name = input("What's your name :");
print("Hello ",name);
print("Thank you for anticipating in this /n Guessing game of our");
print("The question we'd like to ask is: ");
answer = input("What is five plus two? ");

if answer == "7":
	print("Yes the answer is 7");
else:
	print("Sorry the answer is not ", answer, "it's 7");
	
print("Thank you for participating in this game ",name);