import re

txt = 'My phone number is 408-2424-900'

phone = re.search(r'\d\d\d-\d\d\d\d-\d\d\d',txt)

print(phone)
print('The phone number is:\n',phone.group())
phone_pattern = re.compile(r'(\d{3})-(\d{4})-(\d{3})')
results = re.search(phone_pattern, txt)
print('The results are ',results,'\n',results.group())
print('group 1 is:\n ', results.group(1))

print('group list')

for can in results.group():
	print(can)


print('My list of numbers')
txt2 = 'phone numbers 017-0721-327 327-5332-175 574-3421-665, 580-3434-800'

numbers = re.findall(r'\d{3}-\d{4}-\d{3}', txt2)
for num in numbers:
	print(num)

#num_results = re.findall(phone_pattern, txt2)

#for digit in phone_pattern:
#	print(num_results.group(1))