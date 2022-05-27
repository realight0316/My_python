# 프로그래머스 : 가장 큰 수 (https://programmers.co.kr/learn/courses/30/lessons/42746)

# 문제 설명
# 0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.

# 예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 이중 가장 큰 수는 6210입니다.

# 0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때, 
# 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.

# 제한 사항
# numbers의 길이는 1 이상 100,000 이하입니다.
# numbers의 원소는 0 이상 1,000 이하입니다.
# 정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.

# numbers = [6, 10, 2]
# answer = "6210"

numbers = [3, 30, 34, 5, 9]
answer = "9534330"

def solution(numbers):
    num_str = list(map(str, numbers))                   # 주어진 숫자열을 문자열로 바꾸어 리스트화
    print(num_str)
    num_str.sort(key=lambda x: x*3, reverse=True)       # 아래 추가 설명 작성
    return str(int(''.join(num_str)))                   # 만약 num_str이 0,0,0,0이면 정답은 0000이 아닌 0이므로 정수형으로 변경뒤 다시 문자화

result = solution(numbers)
print(f"{answer} / {result}")

# key=lambda x: x[0]을 통해 첫번째 숫자로 정렬하려고 했으나 34,30,3 처럼 되는 경우가 생겼음
# numbers의 원소는 1000이하이므로 문자를 3번 반복하여(*3) 늘려주고 그 다음에 앞자리부터 정렬시킨다
# 34, 3, 30은 343434, 333, 303030이 되고 숫자가 아닌 문자타입이므로 앞자리의 아스키코드 값을 순서로 정렬한다
# 34... 33... 30... 순으로 정렬처리됨