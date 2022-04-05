# generates dictionary that maps letters to other letters
def generateKey(n):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = {}
    cnt = 0
    
    for character in letters:
        key[character] = letters[(cnt+n) % len(letters)]
        cnt += 1
        
    return key

# encryption function
def encrypt(key, message):
    cipher = ""
    for character in message:
        if character in key:
            cipher += key[character]
        elif character == " ":
            cipher += " "
    return cipher    

# get decryption key
# reversing the key, no need to know the shift
def getDecryptionKey(key):
    decKey = {}
    print(key)
    for character in key:
        #print("Letter: ", key[character])
        #print("Maps to: ", character)
        decKey[key[character]] = character
    return decKey
    
###############################################################################

# person 1
key = generateKey(3)
#print("Key: ", key)
message = "YOU ARE AWESOME"
cipher = encrypt(key, message)
#print("Cipher: ", cipher)

decKey = generateKey(26-3)      # 26 letters in the alphabet, must know the shift
#print("Decription key: ", decKey)
message = encrypt(decKey, cipher)
#print("Message: ", message)

# attacker - knowing the key
decKey = getDecryptionKey(key)  # reversing the key, no need to know the shift
message = encrypt(decKey, cipher)
#print("Message: ", message)

# attacker - not knowing the key
print("Cipher: ", cipher)
for i in range(26):
    decKey = generateKey(i)
    message = encrypt(decKey, cipher)
    print(message)


# If you know the algorigthm then you can break the cipher
#
# Crypto Rule 1 - Kerckhoffs' Principle
# the attacker should not be able to break the cipher
# even if they know the algorithm
