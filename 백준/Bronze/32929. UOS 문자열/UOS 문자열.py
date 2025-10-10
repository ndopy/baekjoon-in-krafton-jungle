import sys

x = int(sys.stdin.readline())

message = 'UOS'

location = x % len(message) - 1

print(message[location])