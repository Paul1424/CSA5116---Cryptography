import string

keyword = input("Enter keyword: ").upper()

cipher = ""

for ch in keyword + string.ascii_uppercase:
    if ch.isalpha() and ch not in cipher:
        cipher += ch

text = input("Enter plaintext: ")

table = str.maketrans(
    string.ascii_uppercase + string.ascii_lowercase,
    cipher + cipher.lower()
)

print("Cipher alphabet:", cipher)
print("Ciphertext:", text.translate(table))