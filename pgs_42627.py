# 프로그래머스 : 디스크 컨트롤러 (https://programmers.co.kr/learn/courses/30/lessons/42627)

# 링크에서 이미지와 함께 설명 확인

# 제한 사항
# jobs의 길이는 1 이상 500 이하입니다.
# jobs의 각 행은 하나의 작업에 대한 [작업이 요청되는 시점, 작업의 소요시간] 입니다.
# 각 작업에 대해 작업이 요청되는 시간은 0 이상 1,000 이하입니다.
# 각 작업에 대해 작업의 소요시간은 1 이상 1,000 이하입니다.
# 하드디스크가 작업을 수행하고 있지 않을 때에는 먼저 요청이 들어온 작업부터 처리합니다.

# jobs = [[0, 3], [1, 9], [2, 6]]
# answer = 9
# 입출력 예 설명
# 0ms 시점에 3ms 걸리는 작업 요청이 들어옵니다.
# 1ms 시점에 9ms 걸리는 작업 요청이 들어옵니다.
# 2ms 시점에 6ms 걸리는 작업 요청이 들어옵니다.

jobs = [[0, 10], [2, 10], [9, 10], [15, 2]]
answer = 14

def solution(jobs):
    answer, now = 0, 0                      # 결과, 현재시각

    jobs = sorted(jobs, key=lambda x:x[1])  # 작업 요청 시간보다 작업 소요시간이 중요함, 소요시간으로 정렬
    jobs_len = len(jobs)
    print(jobs)

    while jobs:
        for n, job in enumerate(jobs):      # 작업을 하나씩 조건과 확인하기 위함
            print(n, job)
            if job[0] <= now:               # 해당 작업의 요청시간이 현재 시각과 맞는지 확인
                now += job[1]               # 작업소요시간 + 시작시간 = 작업 이후의 시각
                answer += now - job[0]      # 요청되기 전의 시간은 계산하지 않으므로 지금까지의 시간에서 요청시각 빼기
                jobs.pop(n)                 # 처리된 작업은 리스트에서 제거
                break                       # 리스트가 갱신 되었으므로 for문 탈출, 리스트가 있으면 재시작 없으면 종료
            if n == len(jobs) - 1:          # 작업을 처리하면 for문을 탈출하게됨 즉, 해당 조건에 해당하면 현시각 가능한 작업이 없는 것 
                now += 1                    # 1시간 추가 대기

    answer = answer // jobs_len

    return answer

result = solution(jobs)
print(f"정답: {answer}\n결과: {result}")