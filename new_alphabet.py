from collections import defaultdict

line = input()

alphabet = defaultdict(str, {
    "a": "@",
    "b": "8",
    "c": "(",
    "d": "|)",
    "e": "3",
    "f": "#",
    "g": "6",
    "h": "[-]",
    "i": "|",
    "j": "_|",
    "k": "|<",
    "l": "1",
    "m": "[]\\/[]",
    "n": "[]\\[]",
    "o": "0",
    "p": "|D",
    "q": "(,)",
    "r": "|Z",
    "s": "$",
    "t": "']['",
    "u": "|_|",
    "v": "\\/",
    "w": "\\/\\/",
    "x": "}{",
    "y": "`/",
    "z": "2",
})

translation = ""
for char in line:
    if alphabet[char.lower()]:
        translation += alphabet[char.lower()]
    else:
        translation += char
print(translation)

