# 프로그래머스 : 프린터 (https://programmers.co.kr/learn/courses/30/lessons/42587)

# 현재 대기목록에 있는 문서의 중요도가 순서대로 담긴 배열 priorities와 
# 내가 인쇄를 요청한 문서가 현재 대기목록의 어떤 위치에 있는지를 알려주는 location이 매개변수로 주어질 때, 
# 내가 인쇄를 요청한 문서가 몇 번째로 인쇄되는지 return 하도록 solution 함수를 작성해주세요.

# 제한사항
# 현재 대기목록에는 1개 이상 100개 이하의 문서가 있습니다.
# 인쇄 작업의 중요도는 1~9로 표현하며 숫자가 클수록 중요하다는 뜻입니다.
# location은 0 이상 (현재 대기목록에 있는 작업 수 - 1) 이하의 값을 가지며 대기목록의 가장 앞에 있으면 0, 두 번째에 있으면 1로 표현합니다.



# priorities = [2, 1, 3, 2]
# location = 2
# answer = 1

priorities = [1, 1, 9, 1, 1, 1]
location = 0
answer = 5

# priorities = [3]
# location = 0
# answer = 1

from collections import deque
def solution(priorities, location):
    answer = 0
    queue = deque(priorities)       # queue 스택 사용

    while queue:
        pop = queue.popleft()       # 첫번째 요소 선출
        location -= 1               # 요소가 하나 줄었으므로 목표의 위치도 -1
        if len(queue) != 0 and pop < max(queue):    # 방금 선출한 요소가 마지막이 아닌 경우 and 최우선 요소가 아닌 경우
            queue.append(pop)                       # 큐 뒤쪽으로 재삽입
            if location == -1:                      # 목표요소였으나 출력되지 못하고 뒤로 돌아갔으면
                location = len(queue) -1            # 마지막 인덱스 부여
        else:                       # 출력이 된 경우
            answer += 1             # 횟수 +1
            if location == -1:      # 출력된 요청이 목표요소였다면 반복 종료
                break
    return answer
        

results = solution(priorities, location)
print(f"{answer} / {results}")