import sys

while (True):
    N = int(sys.stdin.readline())

    if N == 0:
        break

    N_str = str(N)
    reversed_N_str = "".join(reversed(N_str))

    if N_str == reversed_N_str:
        print('yes')
    else:
        print('no')