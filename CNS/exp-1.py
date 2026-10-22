text = input("Enter plaintext: ")
key = int(input("Enter key (1-25): "))

result = ""

for ch in text:
    if ch.isupper():
        result += chr((ord(ch) - 65 + key) % 26 + 65)
    elif ch.islower():
        result += chr((ord(ch) - 97 + key) % 26 + 97)
    else:
        result += ch

print("Ciphertext:", result)