# 백준 : 바이러스 (https://www.acmicpc.net/problem/2606)

# 문제
# 신종 바이러스인 웜 바이러스는 네트워크를 통해 전파된다.
# 한 컴퓨터가 웜 바이러스에 걸리면 그 컴퓨터와 네트워크 상에서 연결되어 있는 모든 컴퓨터는 웜 바이러스에 걸리게 된다.

# <그림 1> [https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/upload/images/zmMEZZ8ioN6rhCdHmcIT4a7.png]
# 예를 들어 7대의 컴퓨터가 <그림 1>과 같이 네트워크 상에서 연결되어 있다고 하자. 
# 1번 컴퓨터가 웜 바이러스에 걸리면 웜 바이러스는 2번과 5번 컴퓨터를 거쳐 3번과 6번 컴퓨터까지 전파되어 
# 2, 3, 5, 6 네 대의 컴퓨터는 웜 바이러스에 걸리게 된다. 
# 하지만 4번과 7번 컴퓨터는 1번 컴퓨터와 네트워크상에서 연결되어 있지 않기 때문에 영향을 받지 않는다.

# 어느 날 1번 컴퓨터가 웜 바이러스에 걸렸다. 컴퓨터의 수와 네트워크 상에서 서로 연결되어 있는 정보가 주어질 때, 
# 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에는 컴퓨터의 수가 주어진다. 컴퓨터의 수는 100 이하이고 각 컴퓨터에는 1번 부터 차례대로 번호가 매겨진다. 
# 둘째 줄에는 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수가 주어진다. 
# 이어서 그 수만큼 한 줄에 한 쌍씩 네트워크 상에서 직접 연결되어 있는 컴퓨터의 번호 쌍이 주어진다.

# 출력
# 1번 컴퓨터가 웜 바이러스에 걸렸을 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 첫째 줄에 출력한다.

# 예제 입력 -> 출력 : 4
# 7
# 6
# 1 2
# 2 3
# 1 5
# 5 2
# 5 6
# 4 7

# DFS 혹은 BFS를 통해 1번과 연결된 네트워크를 모두 탐색하는 방식

from collections import deque

def dfs(conct, start, visit):
    visit[start] = True
    for i in conct[start]:
        if visit[i] == False:
            dfs(conct, i, visit)

#39 첫 방문 노드 True로 방문처리
#40 방문한 노드에 연결된 노드 수 만큼 for문 반복
#41 연결된 노드중에 미방문한 노드가 있으면
#42 들어가서 재귀반복

def bfs(conct, start, visit):
    queue = deque([start])
    visit[start] = True
    while queue:
        x = queue.popleft()
        for i in conct[x]:
            if visit[i] == False:
                queue.append(i)
                visit[i] = True

#50 첫 시작노드를 포함한 큐 스택 생성
#51 방문 노드는 True로 방문 기록
#52 큐가 비어지면 종료, bfs는 접근가능한 모든 노드를 방문하기 전에는 큐가 차있음
#53 처음 넣은 노드를 빼기
#54 뺀 노드와 연결된 노드만큼 반복
#55 연결된 노드중에 미방문노드가 있으면 
#56 해당노드 큐 스택에 추가
#57 방문처리

com_n = int(input())                    # 컴퓨터 수
net_n = int(input())                    # 네트워크 연결 수
conct = []                              # 컴퓨터별 연결된 네트워크를 정리할 리스트
for _ in range(com_n+1):                # 컴퓨터 수만큼 리스트 늘리기 (0번째 사용하지 않으려고 +1 했음)
    conct.append([])

for n in range(net_n):
    x, y = map(int, input().split())    # 입력 받은 네트워크 정보를
    conct[x].append(y)                  # 정리해서 어떤 노드들 끼리 연결된건지 리스트에 저장
    conct[y].append(x)
    conct[x].sort()                     # 오름차순으로 정리
    conct[y].sort()

visit = [False] * (len(conct))          # 방문 기록을 위한 False 리스트 (0번째 사용하지 않으려고 +1 했음)
# visit = [False] * (com_n+1)

# dfs(conct, 1, visit)                    # dfs로 탐색하기
bfs(conct, 1, visit)                    # bfs로 탐색하기

print(visit[2:].count(True))            # 0번째는 미사용, 1번째는 시작지점이므로 2번째부터 끝까지 슬라이싱, True갯수 카운트 그리고 출력
