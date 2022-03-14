print("========================================================================")
import zipfile		# built in lib
import shutil
import os
import re

print("1--------------------------------")
# unpack the archive
# unpack myArchive.zip into myArchiveExtracted, file format: zip
#shutil.unpack_archive("unzip_me_for_instructions.zip", "extractedInfo", "zip")


print("2--------------------------------")
# search files for "https:"
#myPath = 'C:\\Users\\Peter\\Documents\\Python\\Workspace\\Course1\\Section13\\ORANGEmission\\extractedInfo'
myPath = 'C:\\Users\\nxf33232\\OneDrive - NXP\\Documents\\Python\\Workspace\\Course1\\Section13\\ORANGEmission\\extractedInfo'
results = []

for folder, subfolders, files in os.walk(myPath):
	print("Seraching folder: ")
	path = folder
	print(path)

	print("Number of files: ", len(files))
	#print(files)

	# go through all folders and files
	for index,title in enumerate(files):
		print("File index: ", index)
		print("File title: ", title)
		
		# read the text
		f = open(path+"\\"+files[index], "r")
		text = f.read()	
		#print("Text:")		
		#print(text)
		#print("\n")
		
		# search each text for https:
		matchObj = re.findall("\w{5}://\S{1,}", text)
		if len(matchObj) > 0:
			print("Found: ", matchObj[0])
			results.append(matchObj)	
		print("\n")
	
# print results
print("Results: ")
for links in results:
	for link in links:
		print(link)
	

print("3--------------------------------")
## instructor solution
#pattern = "https://[-?/_=.\w]+"
#
#def search(file,pattern="https://[-?/_=.\w]+"):
#	f = open(file, "r")
#	text = f.read()
#	
#	if re.search(pattern,text):
#		return re.search(pattern,text)
#	else:
#		return ""
#
#results = []
#
##myPath = 'C:\\Users\\Peter\\Documents\\Python\\Workspace\\Course1\\Section13\\ORANGEmission\\extractedInfo'
#for folder, subfolder, files in os.walk("extractedInfo"):
#	for f in files:
#		full_path = folder+"\\"+f
#		findings = search(full_path)
#		if findings != "":
#			results.append(findings)
#
#for match in results:
#		print(match.group())
#
print("========================================================================")
