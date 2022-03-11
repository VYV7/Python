print("========================================================================")
import requests
import bs4

print("1--------------------------------")
response = requests.get("https://www.thegoldbugs.com/blog")
soup = bs4.BeautifulSoup(response.text, "lxml")
preTagList = soup.select("pre")
blogText = preTagList[0].getText()

print(blogText)
print(len(blogText))


print("2--------------------------------")
letterList = []
takeLetter = False
cntr = 0

# go through all letters
for letter in blogText:
    if takeLetter == True:
        letterList.append(letter)
        takeLetter = False
    if letter == "-":
        cntr += 1
    if cntr == 5:
        takeLetter = True
        cntr = 0
    
print("".join(letterList))






print("========================================================================")
