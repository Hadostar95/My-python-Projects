class Game:

	def __init__(self, ans):
		self.anwser = ['y','Y','n','N']
		self.ans = ans


	def show(self):
		self.anwser.append(ans)
		print(self.anwser)

class HappyB:
	def __init__(self,man):
		self.thisdirc = {
		"brand": 100,
		"halo": 'GGJVHGVHGGHGHGH',
		'color':['fdff','Ace','kjvnjcnj','Give it to me',1000,3.55]


		}
		self.man = man

	def showlist(self):
		for f in self.thisdirc.values():
			print(f)





ans = ''
g = Game(ans)
anwser = g.anwser
h = HappyB('MAn')
brand = h.thisdirc['brand']
halo = h.thisdirc['halo']
color = h.thisdirc['color']
print(brand)
while ans not in anwser:
	ans = input('Type Anwser:    ')
	
	if ans in anwser:
		if ans == anwser[0]:
			print('Yes')
			#print(brand)
		elif ans == anwser[1]:
			print('Number 2')
			#print(halo)
		elif ans == anwser[2]:
			print('Public e')
			#print(color)
		elif ans == anwser[3]:
			print('Hadostar 95')
		else:
			print('keep going')
	if ans == 'Cake':
		print('CAKYY!')
		continue
	else:
		print('Try again')
else:
	print('Thanks for playing')
	g.show()
	h.showlist()