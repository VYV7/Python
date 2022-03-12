print("========================================================================")

print("1--------------------------------")
f = open("practice.txt", "w+")
f.write("test line")
f.close()


print("2--------------------------------")
import os

cwd = os.getcwd()			# get current working directory
print(cwd)
files = os.listdir()
print(files)


print("3--------------------------------")
import shutil				# utilities for dealing with files

# moving files
shutil.move('practice.txt','C:\\Users\\Peter\\Downloads\\testFile.txt')
files = os.listdir()
print(files)
shutil.move('C:\\Users\\Peter\\Downloads\\testFile.txt','C:\\Users\\Peter\\Documents\\Python\\Workspace\\Course1\\Section13\\testFile.txt')
files = os.listdir()
print(files)


print("4--------------------------------")
# deleting files
# os.unlink(path)		# permemently removie file
# os.rmdir(path)		# permemently remove empty folder
# shutil.rmtree(path)	# permemently remove folder

import send2trash		# moving to bin

files = os.listdir()
print(files)

send2trash.send2trash('testFile.txt')

files = os.listdir()
print(files)


print("5--------------------------------")

#myPath = os.getcwd()
myPath = 'C:\\Users\\Peter\\Documents\\Python\\Workspace\\Course1'
#print(myPath)

for folder, subfolders, files in os.walk(myPath):
	print("Current folder: ")
	print(folder)
	
	print("Sub-folders: ")
	for subfolder in subfolders:
		print(subfolder)
	
	print("Files: ")
	for file in files:
		print(files)
	
	print("\n")


print("========================================================================")
