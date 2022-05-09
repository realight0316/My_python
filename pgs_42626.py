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
        heapq.heappush(heap, x)

    while heap[0] < K:
        heapq.heappush(heap, (heapq.heappop(heap) + (heapq.heappop(heap) * 2)))
        answer += 1
        if heap[0] < K and len(heap) == 1:
            return -1
    return answer

result = solution(scoville, K)
print(f"{answer} / {result}")