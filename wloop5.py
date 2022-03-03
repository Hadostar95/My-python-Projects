ans = ['Chicken','Pie','Raman']
anwser = ''

while anwser not in ans:
	anwser = input('Pick anwser \n')
	if anwser in ans:


		if anwser == ans[0]:

			print('Loooove me some chickan!! bakak')
		elif anwser == ans[1]:
			print('Me love Pie Pie Pie PIIIIIIE')

		elif anwser == ans[2]:
			print('Naurto shadow clone Jutsu')
	else:
		print('try again')
	

else:
	print('Done')
	#break


def looper():
	num = int(input('Type number: \n'))
	incby = int(input('increment by:     '))
	i = 0
	while i < num:
		i+=incby
		print(i)


	#while i > num:
	#	i-=incby
		#print(i)

looper()
