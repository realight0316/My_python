# 백준 : 평범한 배낭 (https://www.acmicpc.net/problem/12865)

# 문제
# 이 문제는 아주 평범한 배낭에 관한 문제이다.

# 준서가 여행에 필요하다고 생각하는 N개의 물건이 있다. 각 물건은 무게 W와 가치 V를 가지는데, 
# 해당 물건을 배낭에 넣어서 가면 준서가 V만큼 즐길 수 있다. 
# 아직 행군을 해본 적이 없는 준서는 최대 K만큼의 무게만을 넣을 수 있는 배낭만 들고 다닐 수 있다. 
# 준서가 최대한 즐거운 여행을 하기 위해 배낭에 넣을 수 있는 물건들의 가치의 최댓값을 알려주자.

# 입력
# 첫 줄에 물품의 수 N(1 ≤ N ≤ 100)과 준서가 버틸 수 있는 무게 K(1 ≤ K ≤ 100,000)가 주어진다. 
# 두 번째 줄부터 N개의 줄에 거쳐 각 물건의 무게 W(1 ≤ W ≤ 100,000)와 해당 물건의 가치 V(0 ≤ V ≤ 1,000)가 주어진다.

# 입력으로 주어지는 모든 수는 정수이다.

# 출력
# 한 줄에 배낭에 넣을 수 있는 물건들의 가치합의 최댓값을 출력한다.

# 예제 입력 -> 14
# 4 7
# 6 13
# 4 8
# 3 6
# 5 12

# Kanpsack problem 냅색 알고리즘 문제

import sys

n, k = map(int,sys.stdin.readline().split())
wv = [[0, 0]]                                           # weight, value
dp = [[0 for _ in range(k+1)] for _ in range(n+1)]      # dp와 wv의 인덱스 0은 미사용

for _ in range(n):
    wv.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, n+1):                 # 인덱스 0 미사용, 1부터 사용
    for j in range(1, k+1):
        if wv[i][0] > j:                
            dp[i][j] = dp[i-1][j]
            continue
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-wv[i][0]]+wv[i][1])

# for a in dp:
#     print(a)
print(wv)
print(max(dp[-1]))


#39 1부터 k까지 올라가면서 해당 무게일때의 최대 가치를 찾는다
#38 요소별로 하나씩 넣어보면서 j무게일때 i요소를 사용하면 최댓값인지 확인해본다

#40 해당 요소의 무게가 제한무게를 넘어서는 경우
#41 추가적인 연산이 없기때문에 이전 최댓값을 그대로 가져온다

#44 dp[i-1][j]는 무게제한j일때 직전단계의 최댓값
#   dp[i-1][j-wv[i][0]]+wv[i][1]는 이전 계산한 값들 중에 해당 요소i를 더 추가한 값
#   해당 요소i를 넣으려면 i의 w만큼 무게가 여유가 있어야한다 그래서 현 무게제한j에서 i의 w를 뺀다. (j-wv[i][0])
#   해당 요소가 연산을 했다는 의미가 j가 w보다 크다는 의미라서 뺄셈이 가능함
#   그 뺀 무게일때의 당시 최댓값을 가져와서 i의 v를 더해준다 (+wv[i][1])
#   당시 최댓값이 0이면 자기자신만 사용하는 경우와 동일해짐

#   동일 무게제한 직전단계 최댓값과 무게조건하에 해당 요소 반드시 가져가는 경우를 비교하는 것