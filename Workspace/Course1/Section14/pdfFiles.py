print("========================================================================")
# PyPDF2 is the one of the most popular libs to work with pdfs
# PyPDF2 will not be able to read all PDFs or extract images
# pip install PyPDF2
print("1--------------------------------")
import PyPDF2

file = open("Working_Business_Proposal.pdf", "rb")	# open PDF as a binary file
pdfReader = PyPDF2.PdfFileReader(file)				# create a reader object

print(pdfReader.numPages)
print("\n")

page1 = pdfReader.getPage(0)
print(page1)
print("\n")
page1txt = page1.extractText()
print(page1txt)
print("\n")


print("\n2--------------------------------")
# you can only copy pages and append pages to a PDF file
file = open("Working_Business_Proposal.pdf", "rb")	# open file as a binary
pdfReader = PyPDF2.PdfFileReader(file)				# create the reader object
page1 = pdfReader.getPage(0)						# get page 0
pdfWriter = PyPDF2.PdfFileWriter()					# create the writer object
pdfWriter.addPage(page1)							# add page 0

pdfOutput = open("NewPDFfile.pdf", "wb")	# create a new file
pdfWriter.write(pdfOutput)					# write into that new file
file.close()								# close files
pdfOutput.close()


print("\n3--------------------------------")
file = open("Working_Business_Proposal.pdf", "rb")	# open file as a binary
text = []
pdfReader = PyPDF2.PdfFileReader(file)				# create the reader object

for p in range(pdfReader.numPages):
	page = pdfReader.getPage(p)
	text.append(page.extractText())
	
print(text[2])		# print page 2








print("========================================================================")
