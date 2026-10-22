from collections import Counter

text = input("Enter ciphertext: ")

counts = Counter(
    ch for ch in text if not ch.isspace()
)

print("Symbol frequencies:")

for symbol, count in counts.most_common():
    print(repr(symbol), ":", count)