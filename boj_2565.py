# 백준 : 전깃줄 (https://www.acmicpc.net/problem/2565)

# 문제
# 두 전봇대 A와 B 사이에 하나 둘씩 전깃줄을 추가하다 보니 전깃줄이 서로 교차하는 경우가 발생하였다. 
# 합선의 위험이 있어 이들 중 몇 개의 전깃줄을 없애 전깃줄이 교차하지 않도록 만들려고 한다.

# 예를 들어, < 그림 1 >과 같이 전깃줄이 연결되어 있는 경우 
# A의 1번 위치와 B의 8번 위치를 잇는 전깃줄, 
# A의 3번 위치와 B의 9번 위치를 잇는 전깃줄, 
# A의 4번 위치와 B의 1번 위치를 잇는 전깃줄을 없애면 남아있는 모든 전깃줄이 서로 교차하지 않게 된다.

# 전깃줄이 전봇대에 연결되는 위치는 전봇대 위에서부터 차례대로 번호가 매겨진다. 
# 전깃줄의 개수와 전깃줄들이 두 전봇대에 연결되는 위치의 번호가 주어질 때, 
# 남아있는 모든 전깃줄이 서로 교차하지 않게 하기 위해 없애야 하는 전깃줄의 최소 개수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에는 두 전봇대 사이의 전깃줄의 개수가 주어진다. 전깃줄의 개수는 100 이하의 자연수이다. 
# 둘째 줄부터 한 줄에 하나씩 전깃줄이 A전봇대와 연결되는 위치의 번호와 B전봇대와 연결되는 위치의 번호가 차례로 주어진다. 
# 위치의 번호는 500 이하의 자연수이고, 같은 위치에 두 개 이상의 전깃줄이 연결될 수 없다.

# 출력
# 첫째 줄에 남아있는 모든 전깃줄이 서로 교차하지 않게 하기 위해 없애야 하는 전깃줄의 최소 개수를 출력한다.

# 예제입력 -> 3
# 8
# 1 8
# 3 9
# 2 2
# 4 1
# 6 4
# 10 10
# 9 7
# 7 6

import sys

N = int(sys.stdin.readline())
line = list()
dp = [1]*N
for _ in range(N):
    line.append(list(map(int, sys.stdin.readline().split())))
line.sort()                 # 리스트 오름차순

# print(line)
                    # LIS(Longest Increasing Subsequence, 최장 증가 부분수열)
for x in range(N):
    for y in range(x):
        if line[x][1] > line[y][1] and dp[x] < dp[y]+1:
            dp[x] = dp[y] + 1
        
print(N-max(dp))