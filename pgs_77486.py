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

def solution1(enroll, referral, seller, amount):
    profit = [0 for _ in range(len(enroll))]

    for name, money in zip(seller, amount):
        superior = referral[enroll.index(name)]
        if money * 10 >= 1 and superior != "-":
            profit[enroll.index(name)] += int(money*90)
            fee = int(money*10)
            while fee>=1:
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
    return profit

# 테스트케이스는 통과하지만 효율성저하로 인해 시간 과다소비, 리스트 대신 딕셔너리 사용 필요

def solution2(enroll, referral, seller, amount):
    profit = {name: 0 for name in enroll}               # 인원들의 수익(profit)을 기록할 딕셔너리 {이름: 수익}
    names_dict = dict(zip(enroll, referral))            # 인원들의 이름(enroll)과 상급자를 기록(referral)한 리스트를 딕셔너리로 한데 묶음
    print(profit)
    print(names_dict)
    for n, sale in enumerate(amount):                   # 판매량(amount=sale)이 몇번째(n) 판매자(seller)의 기록인지 확인하기 위해 enumerate 이용
        now = seller[n]                                 # 현 회차(n) 판매량의 주인(seller[n])을 찾아서 now로 배정
        superior = names_dict[now]                      # now의 상급자를 superior에 배정
        print(seller[n], superior)
        if sale * 10 >= 1 and superior != "-":          # 수익 수수료가 소수점인 경우는 제외, 상급자가 "-"인 경우 제외
            profit[now] += sale*90                      # 판매자가 수수료떼고 남은 수익 가져감
            fee = sale*10                               # 수수료 fee
            while fee>=1:                               # 수수료가 0보다 작을 때까지 부과
                if superior != '-':                     # "-"의 수익은 계산하지 않는다. 해당 경우 제외
                    profit[superior] += fee-(fee//10)   # 모든 수익에 수수료가 적용되므로 1/10을 빼고 수익에 추가
                    superior = names_dict[superior]     # 다음 상급자로 넘어가기
                fee = fee//10                           # 올라가는 수수료 계산
        else:                                           # 상급자가 "-"인 경우는 수익을 기록하지 않을 뿐 수수료는 동일하게 부과
            profit[now] += sale*90
    print(profit)
    answer = list(profit.values())                      # profit 딕셔너리의 values만 모아서 리스트화
    return answer

# print(solution(enroll, referral, seller, amount))
answer = solution2(enroll, referral, seller, amount)
print("정답:", result)
print("총익:", answer)