class Animal():
	"""docstring for Animal"""
	def __init__(self):
		print("Animal CREATED")


	def who_am_i(self):
		print('I am an animal')

	def eat(self):
		print('I am eating')

class Dog(Animal):
	"""docstring for Dog"""
	def __init__(self):
		Animal.__init__(self)
		print("DOG CREATED")
	def who_am_i(self):
		print("I am A DOGG")
	def bark(self):
		print("Hello a i am Bond")

		

myanimal= Animal()
myanimal.eat()
mydog = Dog()
myanimal.who_am_i()
mydog.who_am_i()
mydog.bark()