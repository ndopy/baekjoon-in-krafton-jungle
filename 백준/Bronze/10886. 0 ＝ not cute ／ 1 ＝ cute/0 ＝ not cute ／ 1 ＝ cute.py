import sys

N = int(sys.stdin.readline())

cute = 0
not_cute = 0

for _ in range(N):
    vote = int(sys.stdin.readline())

    if vote == 0:
        not_cute += 1
    else:
        cute += 1

if cute > not_cute:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")