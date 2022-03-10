print("========================================================================")
import certifi
import requests
import bs4			# Beautiful Soup 4

print("1--------------------------------")
res = requests.get("http://freshsereneglowinglight.neverssl.com/online")
soup = bs4.BeautifulSoup(res.text, "lxml")
print(soup)

print("2--------------------------------")
# 1. go to the website, right click on an object and select inspect
# 2. get a class or something else that identifies the object you're interested in
# use . or # in from of the name to indicate if it is a class or an ID
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup


TagList = soup.select("a")
print(TagList)

for item in TagList:
	print(item.text)

















print("========================================================================")