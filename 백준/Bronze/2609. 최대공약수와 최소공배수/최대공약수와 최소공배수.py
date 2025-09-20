import sys

a, b = map(int, sys.stdin.readline().split())

def get_gcd(a, b):
    if b == 0:
        return a

    return get_gcd(b, a % b)

gcd = get_gcd(a, b)

lcm = (a * b) // gcd

print(gcd)
print(lcm)