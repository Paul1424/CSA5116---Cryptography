from math import gcd

a, b = map(int, input("Enter a and b: ").split())

a = a % 26
b = b % 26

if gcd(a, 26) != 1:
    print("Invalid a value")
else:
    text = input("Enter plaintext: ")
    result = ""

    for ch in text:
        if ch.isupper():
            result += chr(
                (a * (ord(ch) - 65) + b) % 26 + 65
            )
        elif ch.islower():
            result += chr(
                (a * (ord(ch) - 97) + b) % 26 + 97
            )
        else:
            result += ch

    print("Ciphertext:", result)

print("Allowed a values:",
      [x for x in range(1, 26) if gcd(x, 26) == 1])