# 백준 : 나이트의 이동 (https://www.acmicpc.net/problem/7562)

# 문제
# 체스판 위에 한 나이트가 놓여져 있다. 나이트가 한 번에 이동할 수 있는 칸은 아래 그림에 나와있다.
# 나이트가 이동하려고 하는 칸이 주어진다. 나이트는 몇 번 움직이면 이 칸으로 이동할 수 있을까?

# 입력
# 입력의 첫째 줄에는 테스트 케이스의 개수가 주어진다.

# 각 테스트 케이스는 세 줄로 이루어져 있다. 첫째 줄에는 체스판의 한 변의 길이 l(4 ≤ l ≤ 300)이 주어진다. 체스판의 크기는 l × l이다. 체스판의 각 칸은 두 수의 쌍 {0, ..., l-1} × {0, ..., l-1}로 나타낼 수 있다. 둘째 줄과 셋째 줄에는 나이트가 현재 있는 칸, 나이트가 이동하려고 하는 칸이 주어진다.

# 출력
# 각 테스트 케이스마다 나이트가 최소 몇 번만에 이동할 수 있는지 출력한다.

# 예제 입력
# 3
# 8
# 0 0
# 7 0
# 100
# 0 0
# 30 50
# 10
# 1 1
# 1 1
# 예제 출력
# 5
# 28
# 0

from collections import deque           # BFS 탐색

def bfs():
    queue = deque([start])
    board[start[0]][start[1]] = 1       # 시작지점 방문처리, 1번째 탐색

    while queue:
        x, y = queue.popleft()
        if [x, y] == arriv:             # 목표지점 발견
            print(board[x][y] -1)       # 첫 지점을 1로 지정했으므로 -1
            continue
        for i, j in knight:             # 나이트 이동
            nx = x + i
            ny = y + j
            if 0<=nx<side and 0<=ny<side and board[nx][ny]==0:  # 실존좌표 및 미방문 조건
                queue.append([nx, ny])
                board[nx][ny] = board[x][y] + 1     # 이전보다 n+1번째탐색

for _ in range(int(input())):
    side = int(input())
    start= list(map(int, input().split()))
    arriv= list(map(int, input().split()))

    if start == arriv:                  # 시작과 도착이 동일하면 종료
        print(0)
        continue

    board= [[0] * side for i in range(side)]    # side X side 크기의 체스판

    knight = [-2, -1], [-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2]
                                                # 나이트의 이동범위 위에서부터 시계방향으로 기입했음
    
    bfs()

