class Hello:
#	pie =20
	
	def __init__(self,ls):
		
		self.evan = []
		self.ls = ls
		self.odd = []


	def lst(self):
		
		
		for l in self.ls:
			if l%2==0:
				self.evan.append(l)
			else:
				self.odd.append(l)
		return self.evan
		return self.odd
	def showlist(self):
		print(self.evan)
		print(self.odd)
		print('Hello world')


	def looper(self):
		for a in self.odd:
			print(f'Odd number {a}')
		for b in self.evan:
			print(f'Evan number {b}')



class Love:
	def __init__(self, name):
		self.name = name
	def confess(self):
		con = 'I love you',self.name
		print(con)
		print(f'I love youuuu {self.name}')

l = Love('JUli')
l.confess()

num = int(input('Input number:     '))
h = Hello(range(num))
#print(h.pie)
#print(h.evan)
h.lst()
h.showlist()
h.looper()
print(range(11))

if 9 in range(10):
	print('Hi Hi')
else:
	print('Out of range')

evannum = h.evan
print(evannum)
adder = 0

for add in evannum:
	adder += add
print(adder)