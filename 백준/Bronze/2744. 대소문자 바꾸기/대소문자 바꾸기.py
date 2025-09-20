import sys

word = sys.stdin.readline()
result = ''

for char in word:
    if char.isupper():
        result += char.lower()
    else:
        result += char.upper()

print(result)