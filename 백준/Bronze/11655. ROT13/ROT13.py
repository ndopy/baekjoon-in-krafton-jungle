upper_cases = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lower_cases = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

import sys
S = sys.stdin.readline()

char_list = []
for char in S:
    if char.islower():
        rot13_idx = (lower_cases.index(char) + 13) % 26
        char_list.append(lower_cases[rot13_idx])
    elif char.isupper():
        rot13_idx = (upper_cases.index(char) + 13) % 26
        char_list.append(upper_cases[rot13_idx])
    else:
        char_list.append(char)

print("".join(char_list))