print("========================================================================")
# to send an email message:
#	- connect to an email server
#	- confirm connection
#	- set a protocol
#	- log on
#	- send the maessage
# python lib: smtplib
# SMPT - Simple Mail Transfer Protocol
# example: smtp.gmail.com
print("1--------------------------------")
# establish connection
import smtplib

#create an SMTP object (port 587 uses TLS encryption)
# or use port number 465 (SSL encryption), or none
#smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj = smtplib.SMTP('smtp.gmail.com')
#smtpObj = smtplib.SMTP("smtp.wp.pl", 465)	

# establish connection with the server
response = smtpObj.ehlo()
print(response)

# initialise TLS encryption
response = smtpObj.starttls()
print(response)

# establish connection with the server
response = smtpObj.ehlo()
print(response)


print("\n2--------------------------------")
# log in
import getpass

#email = getpass.getpass("Your email: ")
email = input("Your email: ")
#print(email)
password = getpass.getpass("Your password: ")
#password = input("Your password: ")
#print(password)
response = smtpObj.login(email, password)
print(response)

print("\n3--------------------------------")
# send an email
sender = email
recipient = email
subject = input("Enter the subject line: ")
message = input("Enter the body message: ")
msg = "Subject: " + subject + "\n" + message

response = smtpObj.sendmail(sender, recipient, msg)
print(response)

response = smtpObj.quit()
print(response)







print("========================================================================")