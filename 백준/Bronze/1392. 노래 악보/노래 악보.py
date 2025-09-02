import sys

N, Q = map(int, sys.stdin.readline().strip().split())

scores = []

for score in range(1, N + 1):
    play_time = int(sys.stdin.readline())

    for _ in range(play_time):
        scores.append(score)

for _ in range(Q):
    question = int(sys.stdin.readline())
    print(scores[question])