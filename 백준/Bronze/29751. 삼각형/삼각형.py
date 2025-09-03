import sys

W, H = map(int, sys.stdin.readline().split())

answer = 0.5 * W * H

print(f"{answer:.1f}")