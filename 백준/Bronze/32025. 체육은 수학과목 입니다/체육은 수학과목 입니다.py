import sys

H = int(sys.stdin.readline())
W = int(sys.stdin.readline())

if H < W:
    print(int(H * 100 / 2))
else:
    print(int(W * 100 / 2))
