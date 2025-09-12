import sys

sangdeok_burger = int(sys.stdin.readline())
jungdeok_burger = int(sys.stdin.readline())
hadeok_burger = int(sys.stdin.readline())
coke = int(sys.stdin.readline())
soda = int(sys.stdin.readline())

burgers = [sangdeok_burger, jungdeok_burger, hadeok_burger]
beverages = [coke, soda]

min_burger_price = min(burgers)
min_beverage_price = min(beverages)

print(min_burger_price + min_beverage_price - 50)