import re

txt = 'The rain in Spain'

x = re.search("^The.*Spain$", txt)

if x:
	print('Indeed')

else:
	print('NOOOOOOO')


text = "The agent's phone number is 007-717-4900. Call me. ET phone home ET phone home"

pattern = 'phone'

b = re.search(pattern, text)
print(b)

matches = re.findall(pattern, text)
for match in matches:
	print(match)

print(len(matches))

for e in re.finditer('ET',text):
	print(e.span())
	print(e.start())
	print(e.end())
	print(e.group(),'Phone Home')

#print(len(re.finditer('ET',text)))