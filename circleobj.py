class Circle():
	"""docstring for Circle"""
	pi = 3.14
	def __init__(self, radius=1):
		self.radius = radius
		self.area = radius*radius*self.pi

	def get_cir(self):
		a = self.radius * self.pi * 2
		print(float(a))
		print(float(self.area))
	
my_cir= Circle(30)
my_cir.get_cir()
print(my_cir.pi)
my_cir.radius
my_cir.area