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

from collections import deque

N, M = map(int, input().split())

mymap = []
for _ in range(N):
    mymap.append(list(map(int, input())))

visit = [[[0]*M for _ in range(N)]]*2
        
moving= [[0, -1], [0, 1], [-1, 0], [1, 0]]

def bfs():
    queue = deque([[0, 0, 0]])
    visit[0][0][0] = 1

    while queue:
        n, m, w = queue.popleft()
        if n == N-1 and m == M-1:
            return visit[n][m][w]
        
        for i, j in moving:
            tn = n + i
            tm = m + j
            
            if 0<=tn<N and 0<=tm<M and visit[tn][tm][w]==0:
                print('좌표: ',n,m,'///',tn,tm,'///',mymap[tn][tm])
                if mymap[tn][tm] == 0:
                    print('A')
                    queue.append([tn, tm, w])
                    visit[tn][tm][w] = visit[n][m][w] + 1
                if w == 0 and mymap[tn][tm] == 1:
                    print('B')
                    queue.append([tn, tm, 1])
                    visit[tn][tm][1] = visit[n][m][w] + 1
        print(queue)
    return -1

print(bfs())



