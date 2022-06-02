# 프로그래머스 : 소수 찾기 (https://programmers.co.kr/learn/courses/30/lessons/42839)

# 문제 설명
# 한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.

# 각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 
# 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# numbers는 길이 1 이상 7 이하인 문자열입니다.
# numbers는 0~9까지 숫자만으로 이루어져 있습니다.
# "013"은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.

# numbers	= "17"
# answer = 3

numbers= "011"
answer = 2

from itertools import permutations

def prime_check(n):         # 소수 확인 함수
    if n < 2:               # 0과 1은 소수가 아님
        return False
    for i in range(2, n):   # 2부터 n까지 순회하며
        if n % i == 0:      # n이 i로 나누어 떨어지면 소수가 아님
            return False
    return True             # 위 조건을 모두 통과하면 소수

def solution(numbers):
    answer = 0
    parts = []
    nums = []

    for n in range(1, len(numbers)+1):          # 순열 구하기 (자릿수 1 ~ n+1)
        parts += permutations(numbers, n)       # numbers의 n자리 순열 모두 구해서 parts 리스트에 넣어주기
                                                # permutations(a, b) -> 리스트 a에서 b개의 원소 갯수를 가진 순열 구하기

    for x in set(parts):
        nums.append(int(''.join(x)))            # part의 숫자는 (1,2,3)처럼 나누어져 있으므로 한데모아서 정수화(int)하여 nums에 모으기
    for y in set(nums):                         # set으로 중복숫자 제거하여 하나씩 순회
        if prime_check(y):                      # 해당 숫자가 소수로 판별되면 소수갯수 +1
            answer += 1
    return answer

result = solution(numbers)
print(f"{answer} / {result}")

# Permutation 순열 : 순서를 고려하는 수열, (A, B)와 (B, A)는 다른 수열으로 인식
# Combination 조합 : 순서없이 원소간 조합, (A, B)와 (B, A)는 동일 수열로 인식