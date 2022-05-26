# 프로그래머스 : 튜플 (https://programmers.co.kr/learn/courses/30/lessons/64065)

# [제한사항]
# s의 길이는 5 이상 1,000,000 이하입니다.
# s는 숫자와 '{', '}', ',' 로만 이루어져 있습니다.
# 숫자가 0으로 시작하는 경우는 없습니다.
# s는 항상 중복되는 원소가 없는 튜플을 올바르게 표현하고 있습니다.
# s가 표현하는 튜플의 원소는 1 이상 100,000 이하인 자연수입니다.
# return 하는 배열의 길이가 1 이상 500 이하인 경우만 입력으로 주어집니다.

# s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
# answer = [2, 1, 3, 4]

s = "{{1,2,3},{2,1},{1,2,4,3},{2}}"
answer = [2, 1, 3, 4]

# s = "{{20,111},{111}}"
# answer = [111, 20]

# s = "{{123}}"
# answer = [123]

# s = "{{4,2,3},{3},{2,3,4,1},{2,3}}"
# answer = [3, 2, 4, 1]


def solution(s):
    answer = []
    s = list(map(str, s[2:-2].split('},{')))    # 주어진 문자열에서 앞뒤로 {{와 }} 제외한뒤 괄호별로 스플릿
    
    s2 = []
    for x in s:
        s2.append(x.split(','))                 # 쉼표별로 한번더 스플릿해서 s2에 정리
    s2.sort(key=len)                            # 원소별로 길이를 통해 정렬순서를 유추할 수 있으므로 작은 리스트를 앞으로 보냄

    for i in s2:
        for j in i:                             # 앞리스트, 첫원소부터 하나씩 순회하며 해당 숫자가 answer에 없으면 뒤로 추가
            if int(j) not in answer:
                answer.append(int(j))
        
    return answer

result = solution(s)
print(f"{answer} / {result}")