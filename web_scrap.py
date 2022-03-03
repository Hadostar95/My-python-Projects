import requests
import bs4

result = requests.get("http://www.example.com")

soup = bs4.BeautifulSoup(result.text,'lxml')
title = soup.select('title')[0].getText()
site_paragraphs = soup.select("p")
grab_div = soup.select('div')
grab_sel = soup.select('#toc')
grab_cla = soup.select('.jump_to_nav')
grab_span = soup.select('div_span')
grab_ds = soup.select('div>span')


print(type(result))
print(result.text)

print(soup)
print(title) # select elements
print(site_paragraphs)
print(type(site_paragraphs))
print(site_paragraphs[0].getText()) # gets the string
print(type(site_paragraphs[0]))
print(grab_div)
print(grab_sel)
print(grab_cla)
print(grab_span)
print(grab_ds)