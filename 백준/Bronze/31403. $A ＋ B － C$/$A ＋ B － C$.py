import sys

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())

print(A + B - C)

str_A = str(A)
str_B = str(B)
str_AB = str_A + str_B

print(int(str_AB) - C)