def u_l(w):
	d={"upper": 0, "lower": 0}

	for x in w:
		if x.isupper():
			d["upper"]+=1
		elif x.islower():
			d["lower"]+=1
		else:
	
			pass
	print("Charaters in: ",w)
	print("There are ",d["upper"],"in Caps")
	print("There are ",d["lower"],"in Low")


w="VAHhalla"
u_l(w)