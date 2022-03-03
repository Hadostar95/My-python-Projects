import requests
import bs4

result = requests.get("https://en.wikipedia.org/wiki/Jonas_Salk")

soup = bs4.BeautifulSoup(result.text,'lxml')
img = soup.select('img')
thub = soup.select('.thumbimage')
computer = soup.select('.thumbimage')[0]
print(type(result))
print(result.text)
print('Image file is:\n  ')
print(img)
print(thub)
print('space')
print(computer)
print(computer['class'])
print(computer['src'])
#for i in thub:
#	print(computer.text)