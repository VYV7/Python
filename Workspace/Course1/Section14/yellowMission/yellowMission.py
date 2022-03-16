print("========================================================================")
import csv
import PyPDF2
import re

print("1--------------------------------")
print("CSV File")
# open the CSV file and extract data
file = open("download_link.csv")		# open as a binary
csvData = csv.reader(file)
dataLines = list(csvData)
file.close()

for line in dataLines:
	print(line)


print("\n2--------------------------------")
# extract the download link from the third colum (CSV)
tempList = []
link = ""
for line in dataLines:
	tempList.append(line[2])
	
link = "".join(tempList)
print(link)

print("\n3--------------------------------")
# open the PDF file and extract the text
print("PDF File")
file = open("Contact_Email_Information.pdf", "rb")
pdfReader = PyPDF2.PdfFileReader(file)

numPages = pdfReader.numPages
print("Number of Pages: ", numPages)

# go through all pages and search for an email addr
results = []
for pageNum in range(0, (numPages-1) ):
	page = pdfReader.getPage(pageNum)
	pageText = page.extractText()
	matchObj = re.findall("\S{1,}@\S{1,}.com", pageText)
	if len(matchObj) > 0:
		results.append(matchObj)

print("Email addresses found: ")
for result in results:	
	print(result)












print("========================================================================")