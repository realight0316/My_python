# 백준 : 가장 긴 증가하는 부분 수열 (https://www.acmicpc.net/problem/11053)

# 문제
# 수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.

# 예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 
# 가장 긴 증가하는 부분 수열은 A = {10, 20, 30, 50} 이고, 길이는 4이다.

# 입력
# 첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.

# 둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)

# 출력
# 첫째 줄에 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력한다.

# 예제 입력1 -> 4
# 6
# 10 20 10 30 20 50

import sys
N = int(sys.stdin.readline())
progression = list(map(int, sys.stdin.readline().split()))
DP = [1 for _ in range(N)]      # 부분수열을 만들때 자기자신 포함을 기본으로 보았으므로 기본값1

for i in range(N):              # 수열을 앞부터 비교
    for j in range(i):          # 선택된 숫자의 앞에 위치한 값들과 비교
        if progression[i] > progression[j]:     # 증가하는 수열이므로 현재값이 이전의 값보다 큰지 확인
            DP[i] = max(DP[i], DP[j]+1)         # 증가하는 수열의 조건하에 현재값으로 만든 수열 vs 비교되는 앞선 기존값의 수열 

print(max(DP))                  # 가장 높은 단계를 가진 수열로 출력