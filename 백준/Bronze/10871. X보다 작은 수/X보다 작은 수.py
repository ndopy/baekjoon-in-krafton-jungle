N, X = input().split()
A = list(map(int, input().split()))

for number in A:
    if number < int(X): print(number, end=' ')