# 프로그래머스 : 더 맵게 (https://programmers.co.kr/learn/courses/30/lessons/42626)

import heapq

# scoville = [1, 2, 3, 9, 10, 12]
# K = 7
# answer = 2

scoville = [0, 0, 0, 0]
K = 3
answer = -1

def fail_solution(scoville, K): # 아직 완성되진 않았는데 리스트가 길게 주어지면 효율성 최저
    answer = 0
    while min(scoville) < K and len(scoville) >= 2:
        scoville.sort()
        temp = scoville.pop(0) + (2 * scoville.pop(0))
        scoville.append(temp)
        answer += 1
    if answer == 0:
        return -1
    return answer

def solution(scoville, K):
    answer = 0
    heap = []
    for x in scoville:
        heapq.heappush(heap, x)     # Heap리스트의 자동정렬 특성을 이용

    while heap[0] < K:              # heap의 최저값이 K보다 작으면 반복
        heapq.heappush(heap, (heapq.heappop(heap) + (heapq.heappop(heap) * 2))) # 문제에서 주어진 공식 적용
        answer += 1                 # 1회 누적
        if heap[0] < K and len(heap) == 1:  # 힙이 1개만 남도록 끝까지 돌렸으나 조건에 만족하지 않으면 -1 출력
            return -1
    return answer

result = solution(scoville, K)
print(f"{answer} / {result}")