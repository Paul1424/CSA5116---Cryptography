text = input("Enter plaintext: ")
key = input("Enter keyword: ").upper()

if not key.isalpha():
    raise SystemExit("Keyword must contain letters only")

result = ""
j = 0

for ch in text:
    if ch.isalpha():
        shift = ord(key[j % len(key)]) - 65
        base = 65 if ch.isupper() else 97

        result += chr(
            (ord(ch.upper()) - 65 + shift) % 26 + base
        )

        j += 1
    else:
        result += ch

print("Ciphertext:", result)