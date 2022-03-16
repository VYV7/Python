print("========================================================================")
# CSV - Comma Separated Variables
#		In practice not only commas are used as separators
print("1--------------------------------")
import csv

f = open("download_link.csv")
print(f)

csv_data = csv.reader(f)
print(csv_data)

print("\n2--------------------------------")
# sometimes you can get an error related to encoding.
# In this case you need to specify the correct encoding
f = open("download_link.csv", encoding="utf-8")
csv_data = csv.reader(f)
print(csv_data)
data_lines = list(csv_data)
#print(data_lines)

for row in data_lines[:5]:
	print(row)


print("\n3--------------------------------")
# creating a new file
file = open("newCSVfile.csv", "w", newline="")
csvWriter = csv.writer(file, delimiter=",")
csvWriter.writerow(["col1", "col2", "col3"])
csvWriter.writerows([[1, 2, 3], [4, 5, 6]])
file.close()


print("\n4--------------------------------")
# appending to an existrin file
file = open("newCSVfile.csv", "a", newline="")		# open to append
csvWriter = csv.writer(file)
csvWriter.writerow([7, 8, 9])
file.close()


print("========================================================================")
