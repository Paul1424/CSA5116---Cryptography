square = [
    list("MFHIK"),
    list("UNOPQ"),
    list("ZVWXY"),
    list("ELARG"),
    list("DSTBC")
]

pos = {
    square[r][c]: (r, c)
    for r in range(5)
    for c in range(5)
}

text = input("Enter plaintext: ").upper()

text = "".join(
    "I" if ch == "J" else ch
    for ch in text
    if ch.isalpha()
)

pairs = []
i = 0

while i < len(text):
    a = text[i]

    if i + 1 >= len(text):
        b = "X"
        i += 1
    elif text[i] == text[i + 1]:
        b = "X"
        i += 1
    else:
        b = text[i + 1]
        i += 2

    pairs.append((a, b))

result = ""

for a, b in pairs:
    r1, c1 = pos[a]
    r2, c2 = pos[b]

    if r1 == r2:
        result += square[r1][(c1 + 1) % 5]
        result += square[r2][(c2 + 1) % 5]

    elif c1 == c2:
        result += square[(r1 + 1) % 5][c1]
        result += square[(r2 + 1) % 5][c2]

    else:
        result += square[r1][c2]
        result += square[r2][c1]

print("Prepared pairs:", " ".join(a + b for a, b in pairs))
print("Ciphertext:", result)