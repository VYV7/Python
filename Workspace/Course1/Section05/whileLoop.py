print("========================================================================")

passcode = 0

passcode = int(input("Enter passcode: "))

while passcode != 7:
	print("Incorrect passcode")
	passcode = int(input("Enter passcode: "))
	if passcode == 0:
		break
	
print("Passcode accepted")
print("loop terminated")


	
print("========================================================================")