# 프로그래머스 : 124 나라의 숫자 (https://programmers.co.kr/learn/courses/30/lessons/12899)

# 124 나라가 있습니다. 124 나라에서는 10진법이 아닌 다음과 같은 자신들만의 규칙으로 수를 표현합니다.

# 124 나라에는 자연수만 존재합니다.
# 124 나라에는 모든 수를 표현할 때 1, 2, 4만 사용합니다.
# 예를 들어서 124 나라에서 사용하는 숫자는 다음과 같이 변환됩니다.

# 10진법    124     10진법      124
# 1	        1	    6	       14
# 2	        2	    7	       21
# 3	        4	    8	       22
# 4	        11	    9	       24
# 5	        12	    10	       41
# 자연수 n이 매개변수로 주어질 때, n을 124 나라에서 사용하는 숫자로 바꾼 값을 return 하도록 solution 함수를 완성해 주세요.

# 제한사항
# n은 500,000,000이하의 자연수 입니다.

# n = 1
# answer = 1
# n = 2
# answer = 2
# n = 3
# answer = 4
n = 4
answer = 11

def solution(n):
    answer = ''
    num = [1, 2, 4]     # 3진법의 0,1,2 대신 1,2,4
    while n > 0:
        n -= 1
        answer = str(num[n%3]) + answer     # n진법 계산법으로 answer에 넣기
        n //= 3
    return answer

results = solution(n)
print(f"{answer} / {results}")
