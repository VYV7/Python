print("========================================================================")
import zipfile		# built in lib

f = open("testFile1.txt", "w+")
f.write("some text 1")
f.close()

f = open("testFile2.txt", "w+")
f.write("some text 2")
f.close()

print("1--------------------------------")
# writing to a zip file
compFile = zipfile.ZipFile("compressedFile.zip", "w")	# create and open a zip file
compFile.write("testFile1.txt", compress_type=zipfile.ZIP_DEFLATED)	# add a file to the compressed file
compFile.write("testFile2.txt", compress_type=zipfile.ZIP_DEFLATED) # add a file to the compressed file
compFile.close()


print("2--------------------------------")
# reading from a zip file
zipFile = zipfile.ZipFile("compressedFile.zip")

zipFile.extractall("extracted")	# extract all to a folder "extracted"
zipFile.extract("testFile1.txt")


print("3--------------------------------")

import shutil

# making an archive
# move folder testFolder to a zip archive named myArchive
shutil.make_archive("myArchive", "zip", "testFolder")

# unpacking an archive
# unpack myArchive.zip into myArchiveExtracted, file format: zip
shutil.unpack_archive("myArchive.zip", "myArchiveExtracted", "zip")



print("========================================================================")
