import sys

total_price = int(sys.stdin.readline())

for _ in range(9):
    price = int(sys.stdin.readline())
    total_price -= price

print(total_price)