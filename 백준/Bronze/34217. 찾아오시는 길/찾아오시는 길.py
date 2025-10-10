import sys

A, B = map(int, sys.stdin.readline().split())
C, D = map(int, sys.stdin.readline().split())

hanyang = A + C
yongdap = B + D

if hanyang > yongdap:
    print('Yongdap')
elif hanyang < yongdap:
    print('Hanyang Univ.')
else:
    print('Either')