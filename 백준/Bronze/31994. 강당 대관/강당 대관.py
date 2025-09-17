import sys

max_applicant = 0
seminar_to_open = ''

for _ in range(7):
    seminar, applicant = sys.stdin.readline().split()
    applicant = int(applicant)

    if applicant > max_applicant:
        max_applicant = applicant
        seminar_to_open = seminar

print(seminar_to_open)