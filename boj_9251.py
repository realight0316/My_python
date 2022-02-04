# 백준 : LCS (https://www.acmicpc.net/problem/9251)

# 문제
# LCS(Longest Common Subsequence, 최장 공통 부분 수열)문제는 두 수열이 주어졌을 때, 
# 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.

# 예를 들어, ACAYKP와 CAPCAK의 LCS는 ACAK가 된다.

# 입력
# 첫째 줄과 둘째 줄에 두 문자열이 주어진다. 문자열은 알파벳 대문자로만 이루어져 있으며, 
# 최대 1000글자로 이루어져 있다.

# 출력
# 첫째 줄에 입력으로 주어진 두 문자열의 LCS의 길이를 출력한다.

# 예제 입력 -> 4
# ACAYKP
# CAPCAK

# LCS 알고리즘 참고자료 
# https://velog.io/@emplam27/알고리즘-그림으로-알아보는-LCS-알고리즘-Longest-Common-Substring와-Longest-Common-Subsequence

str1 = list(map(str, input()))
str2 = list(map(str, input()))
dp = [[0 for _ in range(len(str2))] for _ in range(len(str1))]

for i in range(len(str1)):
    for j in range(len(str2)):
        if str1[i] == str2[j]:                      # 1번과 2번의 글자가 동일할때 +1
            if i == 0 or j == 0:                    # 인덱스를 0번부터 모두 사용하다보니 에러를 피하기위해 추가한 조건
                dp[i][j] = dp[i][j] + 1
            else:
                dp[i][j] = dp[i-1][j-1] + 1         # 이전단계까지 공통부분수열 갯수 +1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])  # 동일하지 않으면 현 단계까지 공통부분수열 최대갯수를 계승

# for A in dp:
#     print(A)
# print()

print(max(dp[-1]))      # 갯수를 저장한 dp리스트 마지막줄 최댓값을 출력
