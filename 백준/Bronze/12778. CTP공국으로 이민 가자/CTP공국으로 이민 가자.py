import sys

T = int(sys.stdin.readline())

alphabets = ['_', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

for _ in range(T):
    M_str, type = sys.stdin.readline().split()
    M = int(M_str)

    if type == 'C':
        # 알파벳을 숫자로 바꾸기
        targets = sys.stdin.readline().split()
        for char in targets:
            print(ord(char) - ord('A') + 1, end=' ')
        print()

    else:
        # 숫자를 문자로 바꾸기
        targets = map(int, sys.stdin.readline().split())
        for num in targets:
            print(alphabets[num], end=' ')
        print()

