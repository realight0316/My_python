# 프로그래머스 : 게임 맵 최단거리 (https://programmers.co.kr/learn/courses/30/lessons/1844)

# 게임 맵의 상태 maps가 매개변수로 주어질 때, 
# 캐릭터가 상대 팀 진영에 도착하기 위해서 지나가야 하는 칸의 개수의 최솟값을 return 하도록 solution 함수를 완성해주세요.
# 단, 상대 팀 진영에 도착할 수 없을 때는 -1을 return 해주세요.

# 제한사항
# maps는 n x m 크기의 게임 맵의 상태가 들어있는 2차원 배열로, n과 m은 각각 1 이상 100 이하의 자연수입니다.
# n과 m은 서로 같을 수도, 다를 수도 있지만, n과 m이 모두 1인 경우는 입력으로 주어지지 않습니다.
# maps는 0과 1로만 이루어져 있으며, 0은 벽이 있는 자리, 1은 벽이 없는 자리를 나타냅니다.
# 처음에 캐릭터는 게임 맵의 좌측 상단인 (1, 1) 위치에 있으며, 상대방 진영은 게임 맵의 우측 하단인 (n, m) 위치에 있습니다.

# 최단거리 찾기 = BFS알고리즘

maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
answer = 11

# maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]
# answer = -1

from collections import deque

def solution(maps):
    answer = 0

    N = len(maps)       # y 길이(세로)
    M = len(maps[0])    # x 길이(가로)

    sample = [[-1 for _ in range(M)] for _ in range(N)]     # 이동단계를 기록할 지도
    sample[0][0] = 1                                        # 시작지점 1단 처리

    # 상하좌우 이동
    dy = [-1, 1, 0, 0]
    dx = [ 0, 0,-1, 1]

    queue = deque([[0, 0]])     # 큐에 시작지점 삽입상태로 생성

    while queue:                # 큐 비워질때까지 진행
        i, j = map(int, queue.popleft())    # 선입선출, i세로좌표 / j가로좌표
        
        for num in range(4):    # 상하좌우 이동처리
            nx = j + dx[num]
            ny = i + dy[num]

            if 0 <= nx < M and 0 <= ny < N and maps[ny][nx] == 1:   # 존재하는 좌표 and 이동할 수 있는 좌표
                if sample[ny][nx] == -1:                            # 이동기록이 없는 좌표
                    sample[ny][nx] = sample[i][j] + 1               # 현재 좌표는 이동 전 좌표보다 + 1단계
                    queue.append([ny, nx])                          # 이동할 수 있는 좌표라면 다음이동 시도 위해 큐 삽입

    for q in maps:      # 맵 확인
        print(q)
    print()
    for q in sample:    # 이동 기록 확인
        print(q)

    return sample[-1][-1]   # 가장 마지막 좌표가 도착지점, 단계 리턴

results = solution(maps)
print(f"{answer} / {results}")