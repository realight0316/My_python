# 백준 : DFS와 BFS (https://www.acmicpc.net/problem/1260)

# 문제
# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
# 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고,
# 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

# 입력
# 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다.
# 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다.
# 입력으로 주어지는 간선은 양방향이다.

# 출력
# 첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.

# 예제 입력 1 
# 4 5 1
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4
# 예제 출력 1 
# 1 2 4 3
# 1 2 3 4

# 예제 입력 2 
# 5 5 3
# 5 4
# 5 2
# 1 2
# 3 4
# 3 1
# 예제 출력 2 
# 3 1 2 5 4
# 3 1 4 2 5

# 예제 입력 3 
# 1000 1 1000
# 999 1000
# 예제 출력 3 
# 1000 999
# 1000 999

from collections import deque   # BFS를 위한 deque

def dfs(graph, v, visit, answer):
    visit[v] = True             # 시작노드 v 방문 처리
    answer.append(v)            # 정답 리스트에 방문한 노드 추가
    for i in graph[v]:          # 연결된 노드수 만큼 반복
        if not visit[i]:        # if 방문안했으면
            dfs(graph, i, visit, answer)   # 현위치 시작노드로 취급하여 재귀 
    return answer

def bfs(graph, v, visit, answer):
    queue = deque([v])          # 시작노드를 넣어서 큐 생성
    visit[v] = True             # 시작노드 v 방문 처리
    while queue:                # queue가 비어있으면 종료
        x = queue.popleft()     # 가장 마지막에 들어온 노드 큐에서 빼내기
        answer.append(x)        # 빼낸 노드 정답 리스트에 추가
        for i in graph[x]:      # 빼낸 노드의 간선만큼 반복
            if not visit[i]:    # 방문 안했으면
                queue.append(i) # 큐에 연결노드 넣어주고
                visit[i] = True # 해당 노드 방문처리
    return answer

        

n, m, v = map(int, input().split())     # n 노드갯수, m 간선갯수, v시작노드
graph = [[]]                    # 2차원 리스트 선언
visit = [False] * (n+1)         # 처음엔 모두 미방문처리, 노드 0번 안쓰고 1번부터 쓰기 위해서 n+1
dfs_ans = []
bfs_ans = []

for _ in range(n):              # 노드 갯수만큼 반복
    graph.append([])            # 2차원 리스트

for _ in range(m):              # 제공한 간선수만큼 진행
    x, y = map(int, input().split())    # 간선정보 x와 y에 수신
    graph[x].append(y)          # 해당문제의 간선은 양방향이므로 서로에게 추가
    graph[y].append(x)
    graph[x].sort()
    graph[y].sort()

dfs(graph, v, visit, dfs_ans)
# print('dfs_ans: ', dfs_ans)

visit = [False] * (n+1)         # 선행된 dfs로 모든 노드가 방문처리 되어있어서 다시 초기화
bfs(graph, v, visit, bfs_ans)
# print('bfs_ans: ', bfs_ans)

for ans in dfs_ans:             # 결과출력 양식 맞추기
    print(ans, '', end='')
print()
for ans in bfs_ans:
    print(ans, '', end='')
