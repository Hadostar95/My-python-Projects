import requests
import bs4


base_url = 'http://books.toscrape.com/catalogue/page-{}.html'
#base_url.format('20')
res = requests.get(base_url.format(1))
soup = bs4.BeautifulSoup(res.text,'lxml')
products = soup.select(".product_pod")
#print(base_url.format('20'))

for pg in range(1,21):
	print(base_url.format(pg))

print(soup)
print(products)
print('There are: ',len(products),' Products')



example = products[0]
print(example)
print('HHHHHH')
print(example.select(".star-rating.Three"))
print(type(example.select('a')[1]))
print(example.select('a')[1]['title'])

for bk in products:
	print(example.select('a')[1]['title'])



#two_star_titles = []

#for n in range(1,51):
#	scrape_url = base_url.format(n)
#	res = requests.get(scrape_url)

#	soup = bs4.BeautifulSoup(res.text,'lxml')
#	books = soup.select(".product_pod")

#	for book in books:
#		if len(book.select('star-rating.Two')) != 0:
#			book_title = book.select('a')[1]['title']
#			two_star_titles.append(book_title)
#			#return two_star_titles
#	print(two_star_titles)