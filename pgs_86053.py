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
    answer = -1

    return answer

answer = solution(a, b, g, s, w, t)
print(f"{result} / {answer}")