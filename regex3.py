import re

story = 'The cat is here and the dog is out'
phrase = 'there are 3 numbers 34 inside 5 this sentence'
pattern = r'[^\d]+'
test_phase = 'This is a string!! But it has punctuation. How can we remove it?'

stoserach=re.search(r'cat|dog', story)

print(stoserach)
print(stoserach.group())

find = re.findall(r'at', 'The cat in the hat sat there and went splat')
find1 =re.findall(r'..at', 'The cat in the hat sat there and went splat')
find2 =re.findall(r'^\d', '2 The cat in the hat sat there and went splat')
find3 =re.findall(r'\d$', 'The cat in the hat sat there and went splat 2')
find4 = re.findall(pattern, phrase)
find5 =re.findall(r'[^!.?]+', test_phase)
clean =re.findall(r'[^!.? ]+', test_phase)
print(find)
print(len(find))
print(find1)
print(find2)# prints 1st number in the string
print(find3)# oppisite of find2
print(find4)# removes number
print(find5)# removes punctuation
print(find5)
print(clean)#splits each word
j = ' '.join(clean)
print(j)


tex = 'dbsbds dsdd-aahx chbcbh Hey the code-man long time no-c yah.'
pattern2 = r'[\w]+'
pattern3 = r'[\w]+-[\w]+'
clean2 = re.findall(pattern2, tex)
clean3 = re.findall(pattern3, tex)
print(clean2)
print(clean3)