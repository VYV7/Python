print("========================================================================")
import requests
import bs4			# Beautiful Soup 4

print("1--------------------------------")
res = requests.get("http://www.example.com")

print(type(res.text))
print(res.text)

print("2--------------------------------")
soup = bs4.BeautifulSoup(res.text, "lxml")
print(type(soup))

titleTagList = soup.select("title")
print(type(titleTagList))
print(titleTagList)
print(titleTagList[0])
print(titleTagList[0].getText())










print("========================================================================")