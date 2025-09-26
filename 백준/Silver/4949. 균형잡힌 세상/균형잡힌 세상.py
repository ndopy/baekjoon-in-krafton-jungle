import sys

brackets = {
    ')': '(',
    ']': '['
}

while True:
    stack = []
    strs = sys.stdin.readline().rstrip()
    is_balanced = True

    if strs == '.':
        break

    for char in strs:
        if char == '(' or char == '[':
            stack.append(char)
        elif char == ')' or char == ']':
            if not stack or stack[-1] != brackets[char]:
                is_balanced = False
                break
            else:
                stack.pop()

    if is_balanced:
        if stack:
            print('no')
        else:
            print('yes')
    else:
        print('no')