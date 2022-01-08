# 백준 : 이분 그래프 (https://www.acmicpc.net/problem/1707)

# 문제
# 그래프의 정점의 집합을 둘로 분할하여, 각 집합에 속한 정점끼리는 서로 인접하지 않도록 분할할 수 있을 때, 
# 그러한 그래프를 특별히 이분 그래프 (Bipartite Graph) 라 부른다.

# 그래프가 입력으로 주어졌을 때, 이 그래프가 이분 그래프인지 아닌지 판별하는 프로그램을 작성하시오.

# 입력
# 입력은 여러 개의 테스트 케이스로 구성되어 있는데, 첫째 줄에 테스트 케이스의 개수 K가 주어진다. 
# 각 테스트 케이스의 첫째 줄에는 그래프의 정점의 개수 V와 간선의 개수 E가 빈 칸을 사이에 두고 순서대로 주어진다. 
# 각 정점에는 1부터 V까지 차례로 번호가 붙어 있다. 
# 이어서 둘째 줄부터 E개의 줄에 걸쳐 간선에 대한 정보가 주어지는데v , 
# 각 줄에 인접한 두 정점의 번호 u, v (u ≠ v)가 빈 칸을 사이에 두고 주어진다. 

# 출력
# K개의 줄에 걸쳐 입력으로 주어진 그래프가 이분 그래프이면 YES, 아니면 NO를 순서대로 출력한다.

# 제한
# 2 ≤ K ≤ 5
# 1 ≤ V ≤ 20,000
# 1 ≤ E ≤ 200,000

# 예제 입력
# 2
# 3 2
# 1 3
# 2 3
# 4 4
# 1 2
# 2 3
# 3 4
# 4 2

# 예제 출력
# YES
# NO

from collections import deque
import sys

input = sys.stdin.readline                  # 연산시간을 줄이기 위해 추가 코드

def BFS():
    ans = 0
    for start in range(nodes):              # 비연결 리스트 방지를 위해 모든 노드에서 스타트 시도
        if team[start] == [0]:              # 미방문이면 실행 (0:미방문, 1:팀1, 2:팀2)
            queue = deque([start])
            team[start] = [1]               # 방문 처리
            while queue:
                x = queue.popleft()
                for i in path[x]:
                    if team[i] == [0]:      # 연결노드 방문여부 확인
                        if team[x] == [1]:  # 1이면 2로 등록
                            team[i] = [2]
                        else:               # 2면 1로 등록
                            team[i] = [1]
                        queue.append(i)
                    elif team[i] == team[x]:# 이미 방문을 했으나 두 노드가 동일한 팀이면
                        ans = 1             # 이분그래프 조건을 만족하지 않음
                        break
    if ans == 1:
        print('NO')
    else:
        print('YES')
    

N = int(input())
for n in range(N):
    nodes, edges = map(int, input().split())
    path = [[] for _ in range(nodes)]
    team = [[0] for _ in range(nodes)]
    for i in range(edges):
        i, j = map(int, input().split())
        path[i-1].append(j-1)
        path[j-1].append(i-1)

    BFS()