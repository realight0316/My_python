# 백준 : 정수 삼각형 (https://www.acmicpc.net/problem/1932)

# 문제
#         7
#       3   8
#     8   1   0
#   2   7   4   4
# 4   5   2   6   5
# 위 그림은 크기가 5인 정수 삼각형의 한 모습이다.

# 맨 위층 7부터 시작해서 아래에 있는 수 중 하나를 선택하여 아래층으로 내려올 때, 
# 이제까지 선택된 수의 합이 최대가 되는 경로를 구하는 프로그램을 작성하라. 
# 아래층에 있는 수는 현재 층에서 선택된 수의 대각선 왼쪽 또는 대각선 오른쪽에 있는 것 중에서만 선택할 수 있다.

# 삼각형의 크기는 1 이상 500 이하이다. 삼각형을 이루고 있는 각 수는 모두 정수이며, 범위는 0 이상 9999 이하이다.

# 입력
# 첫째 줄에 삼각형의 크기 n(1 ≤ n ≤ 500)이 주어지고, 둘째 줄부터 n+1번째 줄까지 정수 삼각형이 주어진다.

# 출력
# 첫째 줄에 합이 최대가 되는 경로에 있는 수의 합을 출력한다.

# 예제 입력 -> 30
# 5
# 7
# 3 8
# 8 1 0
# 2 7 4 4
# 4 5 2 6 5

import sys

N = int(sys.stdin.readline())
tri = list()
for _ in range(N):
    tri.append(list(map(int, sys.stdin.readline().split())))

# 위에서부터 내려오면서 이전숫자를 현재숫자에 더해줄것임

for n in range(1, N):                       # 첫번째줄은 이전수가 없으므로 스킵
    for x in range(len(tri[n])):            # 줄마다 원소갯수가 다르므로 len이용
        if x == 0:                          # 첫번째 원소, 마지막 원소는 더할 대상이 하나뿐임
            tri[n][x] += tri[n-1][x]
        elif x == len(tri[n])-1:
            tri[n][x] += tri[n-1][x-1]
        else:                               # 더할 원소가 두개인 경우는 최댓값을 가져감
            tri[n][x] = max(tri[n][x]+tri[n-1][x], tri[n][x]+tri[n-1][x-1])

print(max(tri[N-1]))                        # 삼각형리스트 마지막줄의 최댓값을 출력