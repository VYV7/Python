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
# checking an email
import imaplib
import getpass

# create a session object - make a connection to the server
m = imaplib.IMAP4_SSL("imap.gmail.com")

# log in
email = input("Email: ")
password = getpass.getpass("Password: ")

response = m.login(email, password)
print(response)

print(m.list())

response = m.select("inbox")
print(response)

print("\n2--------------------------------")
# finding an email
#typ, msgNums = m.search(None, "BEFORE 18-Mar-2022")
typ, msgNums = m.search(None, '(SUBJECT "Test email")')
print(typ, " ", msgNums)

emailID = msgNums[0]
print("Email ID:\n", emailID)
response, emailData = m.fetch(emailID, "(RFC822)")
print("Email data:\n", emailData)

rawEmail = emailData[0][1]
rawEmailString = rawEmail.decode("utf-8")


import email
emailMsg = email.message_from_string(rawEmailString)
print("Email msg:\n", emailMsg)

for part in emailMsg.walk():
	print("Email contents:\n", part.get_content_type())

	if part.get_content_type() == "text/plain":		# "text/html" if a link is expected
		body = part.get_payload(decode=True)
		print("Email body:\n", body)
	

m.logout()
m.close()

print("========================================================================")