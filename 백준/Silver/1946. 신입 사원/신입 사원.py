import sys
test_case_count = int(sys.stdin.readline())


for _ in range(test_case_count):
    applicant_count = int(sys.stdin.readline()) # 지원자 숫자
    applicants = []                             # 지원자들의 점수를 저장할 리스트

    # 지원자 리스트에 지원자 정보 담기
    for _ in range(applicant_count):
        document_score, interview_score = map(int, sys.stdin.readline().split())
        applicants.append((document_score, interview_score))

    # 지원자들을 서류 점수 기준으로 오름차순 정렬하기
    applicants.sort(key=lambda x: x[0])

    # 기준이 될 면접 점수 : 이 점수보다 낮아야 선발될 수 있다. -> 무한대로 초기화
    minimum_interview_score = float('Inf')

    # 선발 인원을 저장할 리스트
    selected_applicants = []

    for idx in range(applicant_count):
        document_score, interview_score = applicants[idx]

        if interview_score <= minimum_interview_score:
            selected_applicants.append(applicants[idx])

            # 기준이 될 면접 점수를 업데이트 한다.
            minimum_interview_score = interview_score

    print(len(selected_applicants))