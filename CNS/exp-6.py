text = input("Enter ciphertext: ")
result = ""

# Assumed affine keys: a = 3, b = 15
# Modular inverse of 3 modulo 26 is 9

for ch in text:
    if ch.isupper():
        result += chr(
            (9 * (ord(ch) - 65 - 15)) % 26 + 65
        )
    elif ch.islower():
        result += chr(
            (9 * (ord(ch) - 97 - 15)) % 26 + 97
        )
    else:
        result += ch

print("Candidate plaintext:", result)