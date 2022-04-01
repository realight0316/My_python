# 프로그래머스 : 다단계 칫솔 팔기 (https://programmers.co.kr/learn/courses/30/lessons/77486)

# 문제 너무 길음, 링크에서 직접 설명을 위한 이미지와 함께 확인 필요

enroll   = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]

# seller = ["young", "john", "tod", "emily", "mary"]
# amount = [12, 4, 2, 5, 10]
# result = [360, 958, 108, 0, 450, 18, 180, 1080]

seller = ["sam", "emily", "jaimie", "edward"]
amount = [2, 3, 5, 4]
result = [0, 110, 378, 180, 270, 450, 0, 0]

def solution(enroll, referral, seller, amount):
    answer = []
    profit = [0 for _ in range(len(enroll))]

    for name, money in zip(seller, amount):
        print(name, money*100)
        superior = referral[enroll.index(name)]
        print("상급자:", superior)
        if money * 10 >= 1 and superior != "-":
            profit[enroll.index(name)] += int(money*90)
            fee = int(money*10)
            while fee>=1:
                print(fee*0.1)
                if superior != '-':
                    profit[enroll.index(superior)] += int(fee-(int(fee*0.1)))
                    superior = referral[enroll.index(superior)]
                fee = int(fee*0.1)
            # profit[enroll.index(superior)] += int(money*10)
        elif money*10 >= 1 and superior == "-":
            profit[enroll.index(name)] += int(money*90)
        else:
            profit[enroll.index(name)] += int(money*100)
        
        print("index:", enroll.index(name), "\n")
    print("총익:", profit)
    return answer

# print(solution(enroll, referral, seller, amount))
answer = solution(enroll, referral, seller, amount)
print("정답:", result)

# 시간초과로 인해 리스트 대신 딕셔너리 사용 필요