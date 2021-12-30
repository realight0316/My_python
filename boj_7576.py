# 백준 : 토마토 (https://www.acmicpc.net/problem/7576)

# 문제
# 철수의 토마토 농장에서는 토마토를 보관하는 큰 창고를 가지고 있다. 
# 토마토는 아래의 그림과 같이 격자 모양 상자의 칸에 하나씩 넣어서 창고에 보관한다. 

# 창고에 보관되는 토마토들 중에는 잘 익은 것도 있지만, 아직 익지 않은 토마토들도 있을 수 있다. 
# 보관 후 하루가 지나면, 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은 토마토의 영향을 받아 익게 된다. 
# 하나의 토마토의 인접한 곳은 왼쪽, 오른쪽, 앞, 뒤 네 방향에 있는 토마토를 의미한다. 
# 대각선 방향에 있는 토마토들에게는 영향을 주지 못하며, 토마토가 혼자 저절로 익는 경우는 없다고 가정한다. 
# 철수는 창고에 보관된 토마토들이 며칠이 지나면 다 익게 되는지, 그 최소 일수를 알고 싶어 한다.

# 토마토를 창고에 보관하는 격자모양의 상자들의 크기와 익은 토마토들과 익지 않은 토마토들의 정보가 주어졌을 때, 
# 며칠이 지나면 토마토들이 모두 익는지, 그 최소 일수를 구하는 프로그램을 작성하라. 단, 상자의 일부 칸에는 토마토가 들어있지 않을 수도 있다.

# 입력
# 첫 줄에는 상자의 크기를 나타내는 두 정수 M,N이 주어진다. M은 상자의 가로 칸의 수, N은 상자의 세로 칸의 수를 나타낸다. 
# 단, 2 ≤ M,N ≤ 1,000 이다. 둘째 줄부터는 하나의 상자에 저장된 토마토들의 정보가 주어진다. 
# 즉, 둘째 줄부터 N개의 줄에는 상자에 담긴 토마토의 정보가 주어진다. 하나의 줄에는 상자 가로줄에 들어있는 토마토의 상태가 M개의 정수로 주어진다. 
# 정수 1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸을 나타낸다.

# 토마토가 하나 이상 있는 경우만 입력으로 주어진다.

# 출력
# 여러분은 토마토가 모두 익을 때까지의 최소 날짜를 출력해야 한다. 
# 만약, 저장될 때부터 모든 토마토가 익어있는 상태이면 0을 출력해야 하고, 토마토가 모두 익지는 못하는 상황이면 -1을 출력해야 한다.

# 예제 입력 1 -> 8
# 6 4
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 1

# 예제 입력 2 -> -1
# 6 4
# 0 -1 0 0 0 0
# -1 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 1

# 예제 입력 3 -> 6
# 6 4
# 1 -1 0 0 0 0
# 0 -1 0 0 0 0
# 0 0 0 0 -1 0
# 0 0 0 0 -1 1
from collections import deque

answer = 0
garo, sero = map(int, input().split())
box = list()
for _ in range(sero):
    box.append(list(map(int, input().split())))     # 입력값 모두 받아서 저장, 리스트에서 가로세로 헷갈림 주의

moving_sero = [0, 0, -1, 1]     # 상하좌우로 이동
moving_garo = [-1, 1, 0, 0]

queue = deque()                 # BFS를 위한 큐 형성

for i in range(sero):
    for j in range(garo):
        if box[i][j] == 1:
            queue.append([i,j])     # 익은 토마토(1) 위치에서 동시다발적으로 진행하므로 1의 위치 큐 삽입

while queue:
    temp = queue.popleft()
    x, y = map(int, temp)

    for temp_num2 in range(4):      # 해당 지점을 중심으로 상하좌우 확인
        nx = x + moving_garo[temp_num2]
        ny = y + moving_sero[temp_num2]

        if 0<=nx<sero and 0<=ny<garo and box[nx][ny]==0:    # 존재하는 좌표이며 익지않은 토마토(0)일 경우 진행
                queue.append([nx, ny])
                box[nx][ny] = box[x][y] + 1

for X in box:
    if 0 in X:
        print(-1)
        exit()
    else:
        answer = max(answer, max(X))

# for X in box:
#     for Y in X:
#         if Y == 0:          # 0이 있는지 대조하여 확인
#             print(-1)       # 있으면 -1 출력하고 종료
#             exit()
#         else:               # 없으면 최댓값 단계 찾아서 -1 하고 출력
#             answer = max(answer, Y)

print(answer -1)