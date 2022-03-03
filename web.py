import urllib.request


def web():
	webUrl = urllib.request.urlopen("http://www.google.com")
	print("result code: "+ str(webUrl.getcode()))
	data = webUrl.read()
	print(data)



web()