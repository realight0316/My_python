# 프로그래머스 : 짝지어 제거하기 (https://programmers.co.kr/learn/courses/30/lessons/12973)

# 문제 설명
# 짝지어 제거하기는, 알파벳 소문자로 이루어진 문자열을 가지고 시작합니다. 
# 먼저 문자열에서 같은 알파벳이 2개 붙어 있는 짝을 찾습니다. 
# 그다음, 그 둘을 제거한 뒤, 앞뒤로 문자열을 이어 붙입니다. 
# 이 과정을 반복해서 문자열을 모두 제거한다면 짝지어 제거하기가 종료됩니다. 
# 문자열 S가 주어졌을 때, 짝지어 제거하기를 성공적으로 수행할 수 있는지 반환하는 함수를 완성해 주세요. 
# 성공적으로 수행할 수 있으면 1을, 아닐 경우 0을 리턴해주면 됩니다.

# 예를 들어, 문자열 S = baabaa 라면
# b'aa'baa → 'bb'aa → aa →
# 순서로 문자열을 모두 제거할 수 있으므로 1을 반환합니다.

# 제한사항
# 문자열의 길이 : 1,000,000이하의 자연수
# 문자열은 모두 소문자로 이루어져 있습니다.

s = 'baabaa'
answer = 1

# s = 'cdcd'
# answer = 0

from collections import deque

def solution(s):    # 리스트가 크면 연산과정이 너무 늘어남 / 폐기
    queue = list(map(str, s))
    idx = 1
    while idx <= len(queue)-1:
        if queue[idx-1] == queue[idx]:
            del queue[idx]
            del queue[idx-1]
            idx = 1
        else:
            idx += 1
    if len(queue) == 0:
        return 1
    return 0

def solution2(s):
    s = list(map(str, s))           # 문자열 리스트화
    queue = deque()
    for idx in range(len(s)):       # 리스트 순회
        if len(queue) == 0:         # 스택 비어있으면 우선 삽입
            queue.append(s[idx])
        elif queue[-1] == s[idx]:   # 스택 마지막요소와 현재 요소와 동일하면
            queue.pop()             # 마지막 요소 삭제
        else:
            queue.append(s[idx])    # 요소 다르면 스택 삽입
    if len(queue) == 0:             # 최종스택에서 모두 정리되었으면
        return 1                    # 1
    return 0                        # 아니면 0

results = solution2(s)
print(f"{answer} / {results}")