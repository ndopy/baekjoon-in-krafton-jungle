import sys

N = int(sys.stdin.readline())

message = 'WelcomeToSMUPC'

location = N % len(message) - 1

print(message[location])