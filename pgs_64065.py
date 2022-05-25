# 프로그래머스 : 튜플 (https://programmers.co.kr/learn/courses/30/lessons/64065)

s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
answer = [2, 1, 3, 4]

# s = "{{1,2,3},{2,1},{1,2,4,3},{2}}"
# answer = [2, 1, 3, 4]

# s = "{{20,111},{111}}"
# answer = [111, 20]

# s = "{{123}}"
# answer = [123]

# s = "{{4,2,3},{3},{2,3,4,1},{2,3}}"
# answer = [3, 2, 4, 1]


def solution(s):
    answer = []
    x = list(map(str, s[2:-2].split('},{')))
    print(x)
    
    return answer

result = solution(s)
print(f"{answer} / {result}")