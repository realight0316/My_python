# 프로그래머스 : 네트워크 (https://programmers.co.kr/learn/courses/30/lessons/43162)

# 문제 설명
# 네트워크란 컴퓨터 상호 간에 정보를 교환할 수 있도록 연결된 형태를 의미합니다. 
# 예를 들어, 컴퓨터 A와 컴퓨터 B가 직접적으로 연결되어있고, 컴퓨터 B와 컴퓨터 C가 직접적으로 연결되어 있을 때 
# 컴퓨터 A와 컴퓨터 C도 간접적으로 연결되어 정보를 교환할 수 있습니다. 
# 따라서 컴퓨터 A, B, C는 모두 같은 네트워크 상에 있다고 할 수 있습니다.

# 컴퓨터의 개수 n, 연결에 대한 정보가 담긴 2차원 배열 computers가 매개변수로 주어질 때, 
# 네트워크의 개수를 return 하도록 solution 함수를 작성하시오.

# 제한사항
# 컴퓨터의 개수 n은 1 이상 200 이하인 자연수입니다.
# 각 컴퓨터는 0부터 n-1인 정수로 표현합니다.
# i번 컴퓨터와 j번 컴퓨터가 연결되어 있으면 computers[i][j]를 1로 표현합니다.
# computer[i][i]는 항상 1입니다.

# 입출력 예
# n	computers	                        return
# 3	[[1, 1, 0], [1, 1, 0], [0, 0, 1]]	2
# 3	[[1, 1, 0], [1, 1, 1], [0, 1, 1]]	1

n= 3; computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]] # 2
# n= 3; computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]] # 1

from collections import deque

# BFS 알고리즘을 이용하여 문제풀이
def bfs(nodes, ways, visit):
    answer = 0
    queue = deque([])
    for n in range(nodes):                  # 모든 노드를 대상으로 알고리즘 진행
        if visit[n] == False:               # 노드가 이전에 탐색하면서 방문을 했으면 알고리즘 미진행
            queue.append(n)                 # 이후 일반 BFS탐색법으로 진행
            visit[n] = True
            while queue:                    # queue가 비면 탐색이 종료된 것
                x = queue.popleft()
                for i in ways[x]:
                    if visit[i] == False:
                        queue.append(i)
                        visit[i] = True
            answer += 1                     # queue가 비어서 반복진행이 종료되면 연결된 네트워크 1회 탐색완료 처리
    return answer

ways = []
visit= [False] * n
for _ in range(n):                          # 노드의 수만큼 리스트에 추가
    ways.append([])

for i in range(n):                          # 제공된 computers를 노드별로 정리
    for j in range(n):
        if i != j and computers[i][j] == 1: # i와 j가 동일하면 자기자신이므로 제외, i와 j가 연결되어 있는 경우
            if j not in ways[i] and i not in ways[j]:   # i와 j가 뒤바뀐경우를 제외하여 중복삽입을 방지
                ways[i].append(j)
                ways[j].append(i)

print(bfs(n, ways, visit))                  # 위 함수로 진행하여 answer 출력

