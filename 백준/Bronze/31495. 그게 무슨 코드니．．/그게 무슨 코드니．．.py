import sys

S = sys.stdin.readline().strip()

if S.startswith('"') and S.endswith('"') and len(S) > 2:
    print(S[1:-1])
else:
    print('CE')