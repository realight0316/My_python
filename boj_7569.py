# 백준 : 토마토 (https://www.acmicpc.net/problem/7569)

# 문제
# 철수의 토마토 농장에서는 토마토를 보관하는 큰 창고를 가지고 있다. 
# 토마토는 아래의 그림과 같이 격자모양 상자의 칸에 하나씩 넣은 다음, 상자들을 수직으로 쌓아 올려서 창고에 보관한다.

# 창고에 보관되는 토마토들 중에는 잘 익은 것도 있지만, 아직 익지 않은 토마토들도 있을 수 있다. 
# 보관 후 하루가 지나면, 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은 토마토의 영향을 받아 익게 된다. 
# 하나의 토마토에 인접한 곳은 위, 아래, 왼쪽, 오른쪽, 앞, 뒤 여섯 방향에 있는 토마토를 의미한다. 
# 대각선 방향에 있는 토마토들에게는 영향을 주지 못하며, 토마토가 혼자 저절로 익는 경우는 없다고 가정한다. 
# 철수는 창고에 보관된 토마토들이 며칠이 지나면 다 익게 되는지 그 최소 일수를 알고 싶어 한다.

# 토마토를 창고에 보관하는 격자모양의 상자들의 크기와 익은 토마토들과 익지 않은 토마토들의 정보가 주어졌을 때, 
# 며칠이 지나면 토마토들이 모두 익는지, 그 최소 일수를 구하는 프로그램을 작성하라. 단, 상자의 일부 칸에는 토마토가 들어있지 않을 수도 있다.

# 입력
# 첫 줄에는 상자의 크기를 나타내는 두 정수 M,N과 쌓아올려지는 상자의 수를 나타내는 H가 주어진다. 
# M은 상자의 가로 칸의 수, N은 상자의 세로 칸의 수를 나타낸다. 
# 단, 2 ≤ M ≤ 100, 2 ≤ N ≤ 100, 1 ≤ H ≤ 100 이다. 둘째 줄부터는 가장 밑의 상자부터 가장 위의 상자까지에 저장된 토마토들의 정보가 주어진다. 
# 즉, 둘째 줄부터 N개의 줄에는 하나의 상자에 담긴 토마토의 정보가 주어진다. 
# 각 줄에는 상자 가로줄에 들어있는 토마토들의 상태가 M개의 정수로 주어진다. 
# 정수 1은 익은 토마토, 정수 0 은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸을 나타낸다. 이러한 N개의 줄이 H번 반복하여 주어진다.

# 토마토가 하나 이상 있는 경우만 입력으로 주어진다.

# 출력
# 여러분은 토마토가 모두 익을 때까지 최소 며칠이 걸리는지를 계산해서 출력해야 한다. 
# 만약, 저장될 때부터 모든 토마토가 익어있는 상태이면 0을 출력해야 하고, 토마토가 모두 익지는 못하는 상황이면 -1을 출력해야 한다.

# 예제 입력1 -> -1
# 5 3 1
# 0 -1 0 0 0
# -1 -1 0 1 1
# 0 0 0 1 1

# 예제 입력2 -> 4
# 5 3 2
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 1 0 0
# 0 0 0 0 0

# 예제 입력3 -> 0
# 4 3 2
# 1 1 1 1
# 1 1 1 1
# 1 1 1 1
# 1 1 1 1
# -1 -1 -1 -1
# 1 1 1 -1

from collections import deque

box = list()
answer = 0
queue = deque([])

M, N, H = map(int, input().split())     # 3차원 리스트 필요
for h in range(H):
    sample = []
    for n in range(N):
        sample.append(list(map(int, input().split()))) # 샘플에 2차원 먼저 올리고
        for m in range(M):
            if sample[n][m] == 1:
                queue.append([h,n,m])
    box.append(sample)                  # H기준으로 리스트를 한번씩 더 묶어줌

# box[H][N][M]으로 구성

# 상/하/좌/우/위/아래
dh = [0,0,0,0,1,-1]
dn = [-1,1,0,0,0,0]
dm = [0,0,-1,1,0,0]

# BFS 알고리즘 이용
while queue:
    h, n, m = map(int, queue.popleft())
    for temp_num in range(6):
        th = h + dh[temp_num]
        tn = n + dn[temp_num]
        tm = m + dm[temp_num]
        if 0<=th<H and 0<=tn<N and 0<=tm<M and box[th][tn][tm] == 0:    # 존재하는 좌표인지, 이동 가능한 상태(0)인지
            queue.append([th,tn,tm])
            box[th][tn][tm] = box[h][n][m] + 1
            answer = max(answer, box[th][tn][tm])       # 최고단계 찾기

for i in box:
    for j in i:
        if 0 in j:      # 아직 안익은 토마토(0)이 존재할 경우 -1 출력
            print(-1)
            exit()
if answer == 0:         # 이미 다 익은 상태의 토마토일 경우 0 출력
    print(answer)
else:
    print(answer-1)     # 첫단계에서 이미 1로 시작했기 때문에 결과값에서 -1 계산



# ----------------- 백준 해당문제 질문글에 올라온 연산시간 줄이는 법
# 지금 풀이는 꽤 정석적이기 때문에, 굳이 개선에 시간을 투자하시지 않으셔도 좋을 것 같습니다.
# 그럼에도 개선이 필요하다면 다음과 같은 것들을 해보세요.

# 1. 전체를 함수 안에 넣는다.(놀랍게도 잔역변수 참조가 지역변수 참조보다 느려서 이게 큰 효과가 있는 코드가 많습니다.)

# 2.인덱싱을 줄입니다.
# 22번 줄의 포문을 for u,v,w in zip(dx, dy, dz) 등으로 바꿀 수 있습니다. 
# 아니면 아예 전용 generator를 만들어서 위의 코드보다 못생기지만 빠른 if문을 안에 넣어주면 더 효율적으로 작동할 수 있겠네요.
# 한 가지 더 쥐어짜내라면 BFS는 이런 식으로도 짤 수 있습니다. bfs가 항상 작은 거리의 점부터 방문함을 이용하는 풀이입니다:

# dist = 0
# while q:{
# dist += 1
# for _ in range(len(q)): {
# ...tomato[k][x][y]=dist
# } 
# }