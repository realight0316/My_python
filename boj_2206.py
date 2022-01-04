# 백준 : 벽 부수고 이동하기 (https://www.acmicpc.net/problem/2206)

# 문제
# N×M의 행렬로 표현되는 맵이 있다. 맵에서 0은 이동할 수 있는 곳을 나타내고, 1은 이동할 수 없는 벽이 있는 곳을 나타낸다. 
# 당신은 (1, 1)에서 (N, M)의 위치까지 이동하려 하는데, 이때 최단 경로로 이동하려 한다. 
# 최단경로는 맵에서 가장 적은 개수의 칸을 지나는 경로를 말하는데, 이때 시작하는 칸과 끝나는 칸도 포함해서 센다.

# 만약에 이동하는 도중에 한 개의 벽을 부수고 이동하는 것이 좀 더 경로가 짧아진다면, 벽을 한 개 까지 부수고 이동하여도 된다.

# 한 칸에서 이동할 수 있는 칸은 상하좌우로 인접한 칸이다.

# 맵이 주어졌을 때, 최단 경로를 구해 내는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N(1 ≤ N ≤ 1,000), M(1 ≤ M ≤ 1,000)이 주어진다. 다음 N개의 줄에 M개의 숫자로 맵이 주어진다. 
# (1, 1)과 (N, M)은 항상 0이라고 가정하자.

# 출력
# 첫째 줄에 최단 거리를 출력한다. 불가능할 때는 -1을 출력한다.

# 예제 입력 -> 15
# 6 4
# 0100
# 1110
# 1000
# 0000
# 0111
# 0000

# 예제 입력 -> -1
# 4 4
# 0111
# 1111
# 1111
# 1110

# BFS 이용, 2차원지도 두개(3차원)를 방문확인용으로 만들어서 벽뚫기 사용유무에 따라 구분
from collections import deque

N, M = map(int, input().split())

mymap = []
for _ in range(N):
    mymap.append(list(map(int, input())))

visit = [[[0]*M for i in range(N)] for j in range(2)]
                # 0을 M(가로)만큼 만들어줌
                # 해당 리스트를 N번 반복 
                # 그 2차원리스트를 두번 반복하여 3차원화
                # visit = [W][N][M]으로 구성, W가 벽뚫기 사용 유무(0 or 1)를 판단
        
moving= [[0, -1], [0, 1], [-1, 0], [1, 0]]  # 각각 N과M에 사용하여 좌/우/상/하 이동

def bfs():
    queue = deque([[0, 0, 0]])
    visit[0][0][0] = 1      # 벽뚫기 미사용, (0,0) 좌표

    while queue:
        n, m, w = queue.popleft()
        if n == N-1 and m == M-1:
            return visit[w][n][m]
        for i, j in moving:
            tn = n + i      # 좌우상하 이동
            tm = m + j
            if 0<=tn<N and 0<=tm<M and visit[w][tn][tm]==0:     # 실존좌표 및 해당 위치 미방문시 실행
                if mymap[tn][tm] == 0:                          # 이동가능한 경우
                    queue.append([tn, tm, w])
                    visit[w][tn][tm] = visit[w][n][m] + 1       # 이전 단계에서 +1
                if w == 0 and mymap[tn][tm] == 1:               # 벽뚫기 미사용의 상태에서 벽과 조우한 경우
                    queue.append([tn, tm, 1])                   # 해당 좌표, 벽뚫기 사용했음으로 1
                    visit[1][tn][tm] = visit[w][n][m] + 1       # 이전 단계에서 +1
    return -1               # 모든 조건에 해당되지 않았을 때

print(bfs())



