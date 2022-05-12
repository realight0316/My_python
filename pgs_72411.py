# 프로그래머스 : 메뉴 리뉴얼 (https://programmers.co.kr/learn/courses/30/lessons/72411)

# [문제]
# 각 손님들이 주문한 단품메뉴들이 문자열 형식으로 담긴 배열 orders, 
# "스카피"가 추가하고 싶어하는 코스요리를 구성하는 단품메뉴들의 갯수가 담긴 배열 course가 매개변수로 주어질 때, 
# "스카피"가 새로 추가하게 될 코스요리의 메뉴 구성을 문자열 형태로 배열에 담아 return 하도록 solution 함수를 완성해 주세요.

# [제한사항]
# orders 배열의 크기는 2 이상 20 이하입니다.
# orders 배열의 각 원소는 크기가 2 이상 10 이하인 문자열입니다.
# 각 문자열은 알파벳 대문자로만 이루어져 있습니다.
# 각 문자열에는 같은 알파벳이 중복해서 들어있지 않습니다.
# course 배열의 크기는 1 이상 10 이하입니다.
# course 배열의 각 원소는 2 이상 10 이하인 자연수가 오름차순으로 정렬되어 있습니다.
# course 배열에는 같은 값이 중복해서 들어있지 않습니다.
# 정답은 각 코스요리 메뉴의 구성을 문자열 형식으로 배열에 담아 사전 순으로 오름차순 정렬해서 return 해주세요.
# 배열의 각 원소에 저장된 문자열 또한 알파벳 오름차순으로 정렬되어야 합니다.
# 만약 가장 많이 함께 주문된 메뉴 구성이 여러 개라면, 모두 배열에 담아 return 하면 됩니다.
# orders와 course 매개변수는 return 하는 배열의 길이가 1 이상이 되도록 주어집니다.

# orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
# course = [2,3,4]
# answer = ["AC", "ACDE", "BCFG", "CDE"]

orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
course = [2,3,5]
answer = ["ACD", "AD", "ADE", "CD", "XYZ"]

# orders = ["XYZ", "XWY", "WXA"]
# course = [2,3,4]
# answer = ["WX", "XY"]

# Combination(리스트의 조합을 만들어줌)과 Counter(요소별 중복갯수 세기, 딕셔너리 출력) 함수를 이용하여 문제를 해결

from collections import Counter
from itertools import combinations

def solution(orders, course):
    answer = []
    for x in course:
        temp = []
        for menu in orders:
            com = combinations(sorted(menu), x)     # CA와 AC는 같은 코스임으로 소팅하여 정렬 후 진행
            temp += com                             # 조합을 한데 모아서
        counter_dic = Counter(temp)                 # 카운터를 이용하여 중복갯수 파악

        if len(counter_dic) != 0 and max(counter_dic.values()) != 1:    # 존재하지 않거나, 카운트 값이 1이면 제외
            for i in counter_dic:
                if counter_dic[i] == max(counter_dic.values()):         # 횟수가 최댓값과 같으면
                    j = ''.join(i)                                      # 해당 리스트(조합)을 문자열 하나로 만들고
                    answer.append(j)                                    # 정답 리스트에 추가

    return sorted(answer)                           # 오름차순 정렬하여 정답 제출

results = solution(orders, course)
print(f"{answer} / {results}")