import sys

from collections import deque

S = sys.stdin.readline().strip()

alphabet_stroke = {
    'A': 3, 'B': 2, 'C': 1, 'D': 2, 'E': 3, 'F': 3, 'G': 3,
    'H': 3, 'I': 1, 'J': 1, 'K': 3, 'L': 1, 'M': 3, 'N': 3,
    'O': 1, 'P': 2, 'Q': 2, 'R': 2, 'S': 1, 'T': 2, 'U': 1,
    'V': 1, 'W': 2, 'X': 2, 'Y': 2, 'Z': 1,
}

sum = 0
numbers = deque()

for char in S:
    numbers.append(alphabet_stroke[char])

while (numbers):
    if len(numbers) >= 2:
        num1 = numbers.popleft()
        num2 = numbers.popleft()
        sum = (sum + (num1 + num2)) % 10
    else:
        sum = (sum + numbers.popleft()) % 10

if sum % 2:
    print(f"I'm a winner!")
else:
    print(f"You're the winner?")