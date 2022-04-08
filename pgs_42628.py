# 프로그래머스 : 이중우선순위큐 (https://programmers.co.kr/learn/courses/30/lessons/42628)

# 명령어	수신 탑(높이)
# I 숫자	큐에 주어진 숫자를 삽입합니다.
# D 1	    큐에서 최댓값을 삭제합니다.
# D -1	    큐에서 최솟값을 삭제합니다.

# 큐가 비어있으면 [0,0] 비어있지 않으면 [최댓값, 최솟값]을 return

# 제한사항
# operations는 길이가 1 이상 1,000,000 이하인 문자열 배열입니다.
# operations의 원소는 큐가 수행할 연산을 나타냅니다.
# 원소는 “명령어 데이터” 형식으로 주어집니다.- 최댓값/최솟값을 삭제하는 연산에서 최댓값/최솟값이 둘 이상인 경우, 하나만 삭제합니다.
# 빈 큐에 데이터를 삭제하라는 연산이 주어질 경우, 해당 연산은 무시합니다.

# operations = ["I 16","D 1"]
# answer = [0,0]

# operations = ["I 7","I 5","I -5","D -1"]
# answer = [7,5]

operations = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
answer = 	[333, -45]

def solution(operations):
    heap = []
    for x in operations:
        if x[0] == 'I':                     # 삽입 요청
            heap.append(int(x[2:]))
        if x[0] == 'D' and heap:            # 제거 요청, Heap이 비어있으면 요청 무시
            if x[2:] == '1':                # 최댓값 제거
                m = max(heap)               # 최댓값을 찾고
                heap.pop(heap.index(m))     # 최댓값 인덱스로 제거
            else:
                m = min(heap)               # 최솟값 찾고
                heap.pop(heap.index(m))     # 최솟값 인덱스로 제거
        print(heap)

    if not heap:            # 비어있으면 [0, 0]
        answer = [0, 0]
    else:                   # 힙의 최댓값, 최솟값
        answer = [int(max(heap)), int(min(heap))]
    return answer



# Heap 써서 다시 구성, 진행과정은 동일함 하지만 Heap을 통해 연산속도가 더 빠름 (자동으로 오름차순 정렬처리)
import heapq
def solution2(operations):
    heap = []
    for x in operations:
        if x[0] == 'I':
            heapq.heappush(heap, int(x[2:]))    # heap에 값 삽입
        elif heap:                              # 비어있는 heap이면 요청 무시
            if x[2:] == '1':
                heap.pop(heap.index(heapq.nlargest(1, heap)[0]))    
                                                # heap.nlargest(n, x)[0] : x에서 가장 큰 값 n개로 이루어진 리스트의 첫번째 요소([0])
            else:
                heapq.heappop(heap)             # heap의 첫번째 요소 pop (=최솟값)
        print(heap)
    if heap:
        return [heapq.nlargest(1, heap)[0], heap[0]]
    else:
        return [0, 0]



result= solution2(operations)
print(f"{answer} / {result}")