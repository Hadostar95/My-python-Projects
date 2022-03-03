def u_list(lst):
	x=[]

	for a in lst:

		if a%2 == 0:
			x.append(a)
			
		else:
			print(a)
	print("Evans as a list: ")
	print(x)
	for o in x:
		print(o)

	
def spec_list(li):
	seen_num=[]
	for num in li:
		if num not in seen_num:
			seen_num.append(num)
		else:
			continue

	print(seen_num)





u_list([1,2,3,4,5,6,7,8,9,12,16])

spec_list([2,3,1,4,5,2,22,5,55,55])
