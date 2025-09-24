import sys

S = sys.stdin.readline().strip()

if S[0] == '"' and S[-1] == '"':
    if S[1:-1] == '':
        print('CE')
    else:
        print(S[1:-1])
else:
    print('CE')