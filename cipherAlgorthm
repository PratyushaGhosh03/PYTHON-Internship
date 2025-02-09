#Cipher Algorithm

msg=input('Enter a message ')
shift=int(input("Enter the shift value: "))

encrypted= ""
for char in msg:
	if char.isalpha():
		ascii_offset = 65 if char.isupper() else 97
		encrypted += chr((ord(char) - ascii_offset + shift)%26 + ascii_offset)
	else:
		encrypted +=char

print("Encrypted message: ", encrypted)

decrypted=""
for char in encrypted:
	if char.isalpha():
		ascii_offset = 65 if char.isupper() else 97
		decrypted += chr((ord(char) - ascii_offset - shift)%26 + ascii_offset)
	else:
		decrypted +=char

print("Decrypted message: ", decrypted)
