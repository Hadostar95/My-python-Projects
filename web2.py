import urllib.request
import json

def printResult(data):
	theJSON = json.loads(data)


	if "title" in theJSON["metadata"]:
		print(theJSON["metadata"]["title"])
	count = theJSON["metadata"]["count"]
	print(str(count)+ " events recorded")
	status = theJSON['metadata']['status']
	print("The earthquake status is:  "+str(status))


	for i in theJSON['features']:
		print(i["properties"]['place'])
	print('_____________________________\n')
	
	for j in theJSON['features']:
		if j['properties']['mag']>= 4.0:
			print("%2.1f " % j['properties']['mag'], j ['properties']['place'])
	print('_____________________________\n')

	for k in theJSON['features']:
		print(str(k['properties']['felt'])+" had felt in "+ k['properties']['place'])
	print('_____________________________\n')


def act():

	urlData ="https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_hour.geojson"

	webUrl = urllib.request.urlopen(urlData)
	print("Results code: " + str(webUrl.getcode()))
	if (webUrl.getcode() == 200):
		data = webUrl.read()
		printResult(data)
	else:
		print('recive error, cannot print results')



act()