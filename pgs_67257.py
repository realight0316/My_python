# 프로그래머스 : 수식 최대화 (https://programmers.co.kr/learn/courses/30/lessons/67257)

expression = "100-200*300-500+20"
answer = 60420

# expression = "50*6-3*2"
# answer = 300

from collections import deque
from itertools import permutations

def calculate(exp, ops):
    stack = deque([exp.pop(0)])
    print(ops, '\n')
    while exp:
        pop = exp.pop(0)

        print(pop, exp)
        print(stack, '\n')

        if pop in ['-', '+', '*']:
            if pop == ops[0] and ops[0] == '+':
                x = int(stack.pop()) + int(exp.pop(0))
                stack.append(x)
                continue
            elif pop == ops[0] and ops[0] == '-':
                x = int(stack.pop()) - int(exp.pop(0))
                stack.append(x)
                continue
            elif pop == ops[0] and ops[0] == '-':
                x = int(stack.pop()) * int(exp.pop(0))
                stack.append(x)
                continue
            else:
                stack.append(pop)
                continue
        stack.append(pop)

def solution(expression):
    answer = []
    nums = []
    temp = ''
    ops = ['-', '+', '*']

    for a in expression:
        if a in ops:
            nums.append(int(temp))
            nums += a
            temp = ''
        else:
            temp += a
    nums.append(int(temp))
    print(nums)
    print('-------')
    for op in permutations(ops, 3):
        calculate(nums, op)


    print(nums)
    return answer

result = solution(expression)
print(f"{answer} / {result}")