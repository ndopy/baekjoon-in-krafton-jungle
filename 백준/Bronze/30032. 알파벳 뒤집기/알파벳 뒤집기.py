import sys

N, D = map(int, sys.stdin.readline().split())

alphabets = {
    'd': ('', 'q', 'b'),
    'b': ('', 'p', 'd'),
    'q': ('', 'd', 'p'),
    'p': ('', 'b', 'q')
}

for _ in range(N):
    strs = sys.stdin.readline().strip()
    reversed_strs = ''

    for i in range(N):
        reversed_strs += alphabets[strs[i]][D]

    print(reversed_strs)