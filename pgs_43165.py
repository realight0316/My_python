# 프로그래머스 : 타겟 넘버 (https://programmers.co.kr/learn/courses/30/lessons/43165)

# 문제 설명
# n개의 음이 아닌 정수가 있습니다. 이 수를 적절히 더하거나 빼서 타겟 넘버를 만들려고 합니다. 
# 예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들려면 다음 다섯 방법을 쓸 수 있습니다.

# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3
# 사용할 수 있는 숫자가 담긴 배열 numbers, 타겟 넘버 target이 매개변수로 주어질 때 
# 숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 return 하도록 solution 함수를 작성해주세요.

# 제한사항
# 주어지는 숫자의 개수는 2개 이상 20개 이하입니다.
# 각 숫자는 1 이상 50 이하인 자연수입니다.
# 타겟 넘버는 1 이상 1000 이하인 자연수입니다.

# 입출력 예
# numbers	        target	return
# [1, 1, 1, 1, 1]	3	    5


# numbers = [1,1,1,1,1]
# target  = 3 # 5

numbers = [1,2,1,2]
target  = 2 # 3

# numbers = [1,2,1,2]
# target  = 6 # 1

from collections import deque

def solution(numbers, target):
    answer = 0

    def DFS(step, result):                      # DFS알고리즘 / 해당 단계와 계산값
        nonlocal answer                         # 정답변수 사용
        if step == len(numbers):                # 마지막 단계에 도달한 경우
            if result == target:                # 계산값이 목표값과 동일할 경우에 카운트+1
                answer += 1
            return
                                                # 마지막 단계가 아니므로 단계 하나더 올려서 
                                                # +한번 -한번 재진행
        DFS(step+1, result + numbers[step])
        DFS(step+1, result - numbers[step])
    # DFS(0,0)                                    # 함수 실행

    def BFS():                                  # BFS알고리즘
        nonlocal answer                         # 정답 변수 사용
        queue = deque()
        queue.append([numbers[0],0])            # 넘버스의 첫번째숫자가 +와-일때
        queue.append([-1*numbers[0],0])         # 두가지 상황을 queue에 삽입
        while queue:
            num, step = queue.popleft()         # 계산값과 단계 확인
            step += 1                           # 한단계 상승
            if step < len(numbers):             # 상승해도 마지막단계가 아니면 실행
                queue.append([num + numbers[step], step])   # +와- 두번의 경우를 queue삽입
                queue.append([num - numbers[step], step])
            else:
                if num == target:               # 마지막단계, 계산값과 목표값 동일시 카운트+1
                    answer += 1
        return
    BFS()                                       # 함수 실행

    print(answer)
    return answer

solution(numbers, target)

