# 프로그래머스 : 입국심사 (https://programmers.co.kr/learn/courses/30/lessons/43238)

# 입국심사를 기다리는 사람 수 n, 각 심사관이 한 명을 심사하는데 걸리는 시간이 담긴 배열 times가 매개변수로 주어질 때, 
# 모든 사람이 심사를 받는데 걸리는 시간의 최솟값을 return 하도록 solution 함수를 작성해주세요.

n= 6
times= [7, 10]
answer= 28

# 가장 첫 두 사람은 바로 심사를 받으러 갑니다.
# 7분이 되었을 때, 첫 번째 심사대가 비고 3번째 사람이 심사를 받습니다.
# 10분이 되었을 때, 두 번째 심사대가 비고 4번째 사람이 심사를 받습니다.
# 14분이 되었을 때, 첫 번째 심사대가 비고 5번째 사람이 심사를 받습니다.
# 20분이 되었을 때, 두 번째 심사대가 비지만 6번째 사람이 그곳에서 심사를 받지 않고
# 1분을 더 기다린 후에 첫 번째 심사대에서 심사를 받으면 28분에 모든 사람의 심사가 끝납니다.

# 이분탐색 기초 (https://youtu.be/IfIuG95RH0o)

def solution(n, times):
    answer = 0
    left, right = 1, max(times)*n   # 첫 범위를 최솟값부터 최댓값으로 만들어주는데,
                                    # 최댓값은 가장 비효율적인 심사관이 전인원을 하는 경우로 선택
    while left <= right:            # 더이상 이분할 수 없을때까지 반복
        mid = (left+right)//2       # 중앙값 설정
        cnt = 0
        for i in times:
            cnt += mid // i         # 심사관이 중앙값의 경우 몇명까지 심사할 수 있는지 확인
            if cnt >= n:            # 가능인원수가 n보다 크면 중지
                break
        if cnt >= n:                # 가능인원이 n보다 크므로 시간을 줄여도 됨, 좌측범위에서 재탐색
            right = mid - 1         # 최댓값을 중앙값-1로 설정
            answer = mid            # 정답에 중앙값을 기입
        else:
            left = mid + 1          # 가능인원이 n보다 적으므로 시간을 늘려야 함, 우측범위에서 재탐색
    return answer                   # 반복하여 줄여나갔을때 마지막 범위의 중앙값이 정답

result= solution(n, times)

print("결과:", result)
print("정답:", answer)