import string

alphabet = string.ascii_uppercase
key = input("Enter 26-letter cipher alphabet: ").upper()

if len(key) != 26 or set(key) != set(alphabet):
    print("Invalid cipher alphabet")
else:
    text = input("Enter plaintext: ")

    table = str.maketrans(
        alphabet + alphabet.lower(),
        key + key.lower()
    )

    print("Ciphertext:", text.translate(table))