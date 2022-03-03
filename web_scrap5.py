import requests
import bs4


base_url = 'http://books.toscrape.com/catalogue/page-{}.html'

two_star_titles = []
def booksrc(rate = input('Type rating One - Five:\n')):
	
	for n in range(1,51):

		scrape_url = base_url.format(n)
		res = requests.get(scrape_url)

		soup = bs4.BeautifulSoup(res.text,'lxml')
		books = soup.select(".product_pod")

		for book in books:

			if len(book.select(f'.star-rating.{rate}')) != 0:
				book_title = book.select('a')[1]['title']
				two_star_titles.append(book_title)
				#return two_star_titles
	#print(two_star_titles)
def loopprint():
	booksrc()
	print('*********This is the lis of 2 star books from website*********')
	for bt in two_star_titles:
		print(bt)

loopprint()