# 프로그래머스 : 2 x n 타일링 (https://programmers.co.kr/learn/courses/30/lessons/12900)

# 가로 길이가 2이고 세로의 길이가 1인 직사각형모양의 타일이 있습니다. 
# 이 직사각형 타일을 이용하여 세로의 길이가 2이고 가로의 길이가 n인 바닥을 가득 채우려고 합니다. 
# 타일을 채울 때는 다음과 같이 2가지 방법이 있습니다.

# 타일을 가로로 배치 하는 경우
# 타일을 세로로 배치 하는 경우
# 예를들어서 n이 7인 직사각형은 다음과 같이 채울 수 있습니다.

# 직사각형의 가로의 길이 n이 매개변수로 주어질 때, 
# 이 직사각형을 채우는 방법의 수를 return 하는 solution 함수를 완성해주세요.

# 제한사항
# 가로의 길이 n은 60,000이하의 자연수 입니다.
# 경우의 수가 많아 질 수 있으므로, 경우의 수를 1,000,000,007으로 나눈 나머지를 return해주세요.

n = 2
answer = 5

def solution(n):
    dp = [0 for jinhwan in range(n+1)]  # DP리스트 생성
    dp[1] = 1; dp[2] = 2                # 피보나치 수열 방식과 동일함

    for idx in range(3, len(dp)):
        dp[idx] = (dp[idx-1] + dp[idx-2]) % 1000000007  # 피보나치 수열 진행, 제한사항에 맞게 나눈 나머지 메모리
    return dp[n] 

results = solution(n)
print(f"{answer} / {results}")