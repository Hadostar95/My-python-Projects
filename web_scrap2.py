import requests
import bs4

result = requests.get("https://en.wikipedia.org/wiki/Jonas_Salk")

soup = bs4.BeautifulSoup(result.text,'lxml')
title = soup.select('title')[0].getText()
site_paragraphs = soup.select("p")
grab_div = soup.select('div')
grab_sel = soup.select('#toc')
grab_cla = soup.select('.toctext')
grab_span = soup.select('div_span')
grab_ds = soup.select('div>span')

first_item = soup.select('.toctext')[0]
print(type(result))
print(result.text)

print(soup)
print(title) # select elements
print(site_paragraphs)
print(type(site_paragraphs))
print(site_paragraphs[0].getText()) # gets the string
print(type(site_paragraphs[0]))
print('This is a: ',type(grab_div))
print(grab_div)
print('This is a: ',type(grab_sel))
print(grab_sel)
print('This is a: ',type(grab_cla))
print(grab_cla)
print('This is a: ',type(grab_span))
print(grab_span)
print('This is a: ',type(grab_ds))
print(grab_ds)
for item in soup.select('.toctext'):
	print(item.text)# prints list for TOC
