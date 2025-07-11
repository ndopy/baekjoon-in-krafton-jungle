import sys
count = input()
answer_sheets = list(map(str, sys.stdin.read().split()))

def get_score(answers):
    score = 0
    right_count = 0

    for answer in answers:
        if answer == 'O':
            right_count += 1
            score += right_count
        else:
            right_count = 0

    print(score)

for sheet in answer_sheets:
    get_score(sheet)