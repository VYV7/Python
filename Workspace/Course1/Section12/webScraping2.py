print("========================================================================")
import certifi
import requests
import bs4			# Beautiful Soup 4

print("1--------------------------------")
# send the request
res = requests.get("https://en.wikipedia.org/wiki/Room_641A")
soup = bs4.BeautifulSoup(res.text, "lxml")
print(soup)

print("2--------------------------------")
# 1. go to the website, right click on an object and select inspect
# 2. get a class or something else that identifies the object you're interested in
# use . or # in from of the name to indicate if it is a class or an ID
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup

# soup.select("div")            elements with div tag
# soup.select("#IDname")        element with the ID IDname
# soup.select(".className")     elements with the CSS class name className
# soup.select("div span")       elements named span within div
# soup.select("div > span`")    elements named span directly under div


TagList = soup.select(".mw-headline")
print(TagList)

print("\n")

for item in TagList:
	print(item.text)
	

















print("========================================================================")
