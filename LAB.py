  //exp-1
def caesar_encrypt(text, k):
    result = ""

    for ch in text:
        if ch.isupper():
            result += chr((ord(ch) - ord('A') + k) % 26 + ord('A'))
        elif ch.islower():
            result += chr((ord(ch) - ord('a') + k) % 26 + ord('a'))
        else:
            result += ch

    return result


text = input("Enter plaintext: ")
k = int(input("Enter key (1-25): "))

ciphertext = caesar_encrypt(text, k)

print("Ciphertext:", ciphertext)

//exp-2
def encrypt(text, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    for ch in text.upper():
        if ch in alphabet:
            index = alphabet.index(ch)
            result += key[index]
        else:
            result += ch

    return result


plaintext = input("Enter plaintext: ")
key = input("Enter 26-letter substitution key: ").upper()

if len(key) != 26 or len(set(key)) != 26:
    print("Invalid key! Key must contain 26 unique letters.")
else:
    ciphertext = encrypt(plaintext, key)
    print("Ciphertext:", ciphertext)
//exp-3
def create_matrix(key):
    key = key.upper().replace("J", "I")

    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

    letters = ""

    for ch in key + alphabet:
        if ch.isalpha() and ch not in letters:
            letters += ch

    matrix = []

    for i in range(0, 25, 5):
        matrix.append(letters[i:i+5])

    return matrix


def find_position(matrix, letter):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == letter:
                return row, col


def prepare_text(text):
    text = text.upper().replace("J", "I")
    text = ''.join(ch for ch in text if ch.isalpha())

    result = ""
    i = 0

    while i < len(text):
        a = text[i]

        if i + 1 < len(text):
            b = text[i + 1]

            if a == b:
                result += a + "X"
                i += 1
            else:
                result += a + b
                i += 2
        else:
            result += a + "X"
            i += 1

    return result


def playfair_encrypt(text, matrix):
    text = prepare_text(text)
    result = ""

    for i in range(0, len(text), 2):
        a = text[i]
        b = text[i + 1]

        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)

        # Same row
        if r1 == r2:
            result += matrix[r1][(c1 + 1) % 5]
            result += matrix[r2][(c2 + 1) % 5]

        # Same column
        elif c1 == c2:
            result += matrix[(r1 + 1) % 5][c1]
            result += matrix[(r2 + 1) % 5][c2]

        # Rectangle
        else:
            result += matrix[r1][c2]
            result += matrix[r2][c1]

    return result


key = input("Enter key: ")
plaintext = input("Enter plaintext: ")

matrix = create_matrix(key)

print("\nPlayfair Matrix:")

for row in matrix:
    print(" ".join(row))

ciphertext = playfair_encrypt(plaintext, matrix)

print("\nCiphertext:", ciphertext)
//exp-4
def vigenere_encrypt(text, key):
    result = ""
    key = key.upper()

    key_index = 0

    for ch in text.upper():

        if ch.isalpha():
            p = ord(ch) - ord('A')
            k = ord(key[key_index % len(key)]) - ord('A')

            c = (p + k) % 26

            result += chr(c + ord('A'))

            key_index += 1

        else:
            result += ch

    return result


plaintext = input("Enter plaintext: ")
key = input("Enter key: ")

ciphertext = vigenere_encrypt(plaintext, key)

print("Ciphertext:", ciphertext)
//exp-5
def affine_encrypt(text, a, b):
    result = ""

    for ch in text.upper():

        if ch.isalpha():
            p = ord(ch) - ord('A')

            c = (a * p + b) % 26

            result += chr(c + ord('A'))

        else:
            result += ch

    return result


text = input("Enter plaintext: ")
a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))

ciphertext = affine_encrypt(text, a, b)

print("Ciphertext:", ciphertext)

