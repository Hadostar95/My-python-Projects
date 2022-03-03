def withdraw_mon(cur_bal, amount):
	if cur_bal >= amount:
		cur_bal = cur_bal - amount
		return cur_bal


bal = withdraw_mon(188,100)
if bal <= 50:
	print("The current balance is: ", bal);
	print("We need to make a deposit")
else:
	print("The current balance is: ", bal);
	print("Nothing to see here");
	