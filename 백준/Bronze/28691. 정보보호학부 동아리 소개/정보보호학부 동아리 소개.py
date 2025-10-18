import sys

char = sys.stdin.readline().strip()

clubs = {
    'M': 'MatKor',
    'W': 'WiCys',
    'C': 'CyKor',
    'A': 'AlKor',
    '$': '$clear'
}

print(clubs[char])