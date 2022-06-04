# 프로그래머스 : 수식 최대화 (https://programmers.co.kr/learn/courses/30/lessons/67257)

expression = "100-200*300-500+20"
answer = 60420

# expression = "50*6-3*2"
# answer = 300

from collections import deque
from itertools import permutations
import re

def calculate_cancel(expression, ops):          # 짜다가 취소하고 재작성
    result = []
    stack = deque()

    print(ops, '\n')

    for i in range(3):
        exp = expression[:]
        stack.append(exp.pop(0))
        while exp:
            
            pop = exp.pop(0)

            print(stack)
            print(pop, exp, '\n')

            if pop in ['-', '+', '*']:
                if pop == ops[i] and ops[i] == '+':
                    x = int(stack.pop()) + int(exp.pop(0))
                    stack.append(x)
                    continue
                elif pop == ops[i] and ops[i] == '-':
                    x = int(stack.pop()) - int(exp.pop(0))
                    stack.append(x)
                    continue
                elif pop == ops[i] and ops[i] == '*':
                    x = int(stack.pop()) * int(exp.pop(0))
                    stack.append(x)
                    continue
                else:
                    stack.append(pop)
                    continue
            stack.append(pop)

    print(stack)
    return max(result)

def calculate(expression, operations):      # 문자열과 연산자 우선순위 리스트 수신
    answer = 0
    exp = expression[:]                     # 문자열 복사
    for op in operations:                   # 우선순위 높은 연산자부터 계산한다
        while op in exp:                    # 해당 연산자가 문자열에 존재하지 않을 때까지 계산 진행
            i = exp.index(op)               # 문자열 중 op연산자의 최선위치
            exp[i-1] = str(eval(exp[i-1] + op + exp[i+1]))      # 연산자를 기준으로 앞뒤 숫자를 계산하여 앞포지션에 삽입
            del exp[i:i+2]                  # 이후 연산자와 숫자를 제거해준다
    return abs(int(exp[0]))                 # 계산 결과를 정답에 넣어준다 / 음수는 절댓값 처리

def solution(expression):
    answer = []
    ops = ['-', '+', '*']

    expression = re.split('([-+*])', expression)        # 연산자를 기준으로 문자열을 분해

    print(expression)
    print('-------')

    for op in permutations(ops, 3):                     # ops 연산자 리스트의 3개짜리 순열을 생성
        answer.append(calculate(expression, op))        # 순열별로 우선 순위를 적용하여 계산 진행 (50번줄 코드)

    print(answer)

    return max(answer)                      # 연산자 순위별 결과값리스트에서 최댓값 출력

result = solution(expression)
print(f"{answer} / {result}")