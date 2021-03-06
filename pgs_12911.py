# 프로그래머스 : 다음 큰 숫자 (https://programmers.co.kr/learn/courses/30/lessons/12911)

# 문제 설명
# 자연수 n이 주어졌을 때, n의 다음 큰 숫자는 다음과 같이 정의 합니다.

# 조건 1. n의 다음 큰 숫자는 n보다 큰 자연수 입니다.
# 조건 2. n의 다음 큰 숫자와 n은 2진수로 변환했을 때 1의 갯수가 같습니다.
# 조건 3. n의 다음 큰 숫자는 조건 1, 2를 만족하는 수 중 가장 작은 수 입니다.
# 예를 들어서 78(1001110)의 다음 큰 숫자는 83(1010011)입니다.

# 자연수 n이 매개변수로 주어질 때, n의 다음 큰 숫자를 return 하는 solution 함수를 완성해주세요.

# 제한 사항
# n은 1,000,000 이하의 자연수 입니다.

n = 78
answer = 83

# n = 15
# answer = 23

def solution(n):
    answer = 0
    cntn = bin(n).count('1')        # n 이진화 (ex. 78 = 0b1001110)
    x = n                           # n < x <= 1000000 으로 하나씩 올리면서 찾을 것임
    cntx = 0                        # x 이진수의 1 갯수
    while cntn != cntx:             # n과 x의 이진수 1갯수가 같은 순간 반복 종료
        x += 1                      # 하나씩 올리면서 찾기
        cntx = bin(x).count('1')    # x이진화의 1 갯수 찾기
    return x
    
results = solution(n)
print(f"{answer} / {results}")

# 더 금방 작성 할 수 있었는데 이것저것 사족을 붙여서 효율성테스트에서 몇번 떨어졌었음
# 예상만 하지말고 한번 돌려보고 확인해보는게 필요할 듯, 알고리즘은 금방 짰음
