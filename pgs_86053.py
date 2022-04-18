# 프로그래머스 : 금과 은 운반하기 (https://programmers.co.kr/learn/courses/30/lessons/86053)
# 문제 해설 : https://prgms.tistory.com/101 (해당 링크 3번문제)

a= 10       # 필요 금
b= 10       # 필요 은
g= [100]    # 도시 금 물량
s= [100]    # 도시 은 물량
w= [7]      # 1회 운반 무게
t= [10]     # 편도 이동시간
result= 50  

# a= 90
# b= 500
# g= [70,70,0]
# s= [0,0,500]
# w= [100,100,2]
# t= [4,8,1]
# result= 499

# 제한사항
# 0 ≤ a, b ≤ 10^9
# 1 ≤ g의 길이 = s의 길이 = w의 길이 = t의 길이 = 도시 개수 ≤ 10^5
# 0 ≤ g[i], s[i] ≤ 10^9
# 1 ≤ w[i] ≤ 10^2
# 1 ≤ t[i] ≤ 10^5
# a ≤ g의 모든 수의 합
# b ≤ s의 모든 수의 합

def solution(a, b, g, s, w, t):
    answer = 4 * 10**14 + 10**5
    start = 0
    end = 4 * 10**14 + 10**5        # (2*10^5)*(2*10^9)+10^5, (편도 시간*2)*(금과 은 두번)+마지막 편도시간

    while start <= end:
        mid = (start + end) // 2
        gmax, gmin, smax, smin = 0, 0, 0, 0     # 금 최대운반량, 금 최소운반량, 은 최대운반량, 은 최소운반량

        for i, ti in enumerate(t):
            x = (mid-ti) // (2*ti) + 1      #  해당 시간 내 가능 운송횟수 = (값-편도1회) // (왕복시간) + 앞에서 뺀 편도횟수 1
            gmax += g[i] if g[i] - x * w[i] <= 0 else x * w[i]   # 각각 운반가능량이 소지물량을 상회하면 최대운반량은 소지물량과 같음
            smax += s[i] if s[i] - x * w[i] <= 0 else x * w[i]   # 그렇지 않으면 운반가능량이 최대운반량이 된다
            gmin += min(g[i], abs(s[i] - x * w[i])) if s[i] - x * w[i] <= 0 else 0   # 은(금)을 최대운반을 하고 남은 잔여 가능운반량이 금(은)의 최소운반량이다
            smin += min(s[i], abs(g[i] - x * w[i])) if g[i] - x * w[i] <= 0 else 0   # 최대운반을 하고도 은(금)이 남았다면 더이상 금(은)은 운반할 수 없으므로 0

        # 금을 a무게 이상 운반 할 수 있으면 그 아래 무게는 전부 운반 가능
        # a+b 무게를 운반 할 수 있다면 금을 a만큼 운반하고 나머지는 b운반에 사용 가능
        if gmax >= a and smax >= b and gmax + smin >= a + b:
            end = mid - 1
            try:
                answer = min(answer, mid)
            except:
                answer = mid
        else:
            start = mid + 1

    return answer

answer = solution(a, b, g, s, w, t)
print(f"{result} / {answer}")