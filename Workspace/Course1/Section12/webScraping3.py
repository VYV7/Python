print("========================================================================")
import requests
import bs4			# Beautiful Soup 4

print("1--------------------------------")
# send the request
res = requests.get("https://en.wikipedia.org/wiki/Cicada_3301")
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


image_info = soup.select(".thumbimage")
print(image_info)

print("\n")

circada = image_info[0]
print(circada)

image_link = circada["src"]
print(image_link)

circada_image = requests.get(("http:" + image_link), "lxml")
#print(circada_image.content)
	
# create a jpg file  
f = open("circada_image_new.jpg", "wb")
# store the image in that file
f.write(circada_image.content)
f.close()

f.open()














print("========================================================================")
