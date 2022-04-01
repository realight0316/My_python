# 프로그래머스 : 다단계 칫솔 팔기 (https://programmers.co.kr/learn/courses/30/lessons/77486)

# 문제 너무 길음, 링크에서 직접 설명을 위한 이미지와 함께 확인 필요

enroll   = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]

seller = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]
result = [360, 958, 108, 0, 450, 18, 180, 1080]

# seller = ["sam", "emily", "jaimie", "edward"]
# amount = [2, 3, 5, 4]
# result = [0, 110, 378, 180, 270, 450, 0, 0]


def solution(enroll, referral, seller, amount):
    answer = []
    profit = [[0]for _ in range(len(enroll))]
    for name, money in zip(seller, amount):
        print(name, money*100)
        if money * 0.1 >= 1:
            profit[int(enroll.index(name))] += money*0.1
        print("index:", enroll.index(name))
    return answer

print("정답:", result)
print(solution(enroll, referral, seller, amount))