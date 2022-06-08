# 프로그래머스 : 위장 (https://programmers.co.kr/learn/courses/30/lessons/42578)

# 스파이가 가진 의상들이 담긴 2차원 배열 clothes가 주어질 때 서로 다른 옷의 조합의 수를 return 하도록 solution 함수를 작성해주세요.

# 제한사항
# clothes의 각 행은 [의상의 이름, 의상의 종류]로 이루어져 있습니다.
# 스파이가 가진 의상의 수는 1개 이상 30개 이하입니다.
# 같은 이름을 가진 의상은 존재하지 않습니다.
# clothes의 모든 원소는 문자열로 이루어져 있습니다.
# 모든 문자열의 길이는 1 이상 20 이하인 자연수이고 알파벳 소문자 또는 '_' 로만 이루어져 있습니다.
# 스파이는 하루에 최소 한 개의 의상은 입습니다.

# clothes	= [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
# answer = 5

clothes	= [["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]
answer = 3

from itertools import combinations, product

def solution(clothes):
    answer = 0
    dic = {}

    for c in clothes:
        if c[1] in dic.keys():
            dic[c[1]].append(c[0])
        else:
            dic[c[1]] = [c[0]]
        answer += 1
    print(dic, len(dic))

    # com = list(combinations(dic.values(), len(dic)))
    com = list(product(*(dic[a] for a in dic)))
    print(com)
    answer += len(list(com))
    print(len(com))
    return answer

result = solution(clothes)
print(f"{answer} / {result}")