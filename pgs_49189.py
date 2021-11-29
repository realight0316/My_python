# 프로그래머스 : 가장 먼 노드 (https://programmers.co.kr/learn/courses/30/lessons/49189)

# 문제 설명
# n개의 노드가 있는 그래프가 있습니다. 각 노드는 1부터 n까지 번호가 적혀있습니다. 1번 노드에서 가장 멀리 떨어진 노드의 갯수를 구하려고 합니다.
# 가장 멀리 떨어진 노드란 최단경로로 이동했을 때 간선의 개수가 가장 많은 노드들을 의미합니다.

# 노드의 개수 n, 간선에 대한 정보가 담긴 2차원 배열 vertex가 매개변수로 주어질 때, 1번 노드로부터 가장 멀리 떨어진 노드가 몇 개인지를 return 하도록 solution 함수를 작성해주세요.

# 제한사항
# 노드의 개수 n은 2 이상 20,000 이하입니다.
# 간선은 양방향이며 총 1개 이상 50,000개 이하의 간선이 있습니다.
# vertex 배열 각 행 [a, b]는 a번 노드와 b번 노드 사이에 간선이 있다는 의미입니다.

# 입출력 예
# n     : 6
# vertex: [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
# return: 3

# 입출력 예 설명
# 예제의 그래프를 표현하면 아래 그림과 같고, 1번 노드에서 가장 멀리 떨어진 노드는 4,5,6번 노드입니다.
# (https://grepp-programmers.s3.amazonaws.com/files/ybm/fadbae38bb/dec85ab5-0273-47b3-ba73-fc0b5f6be28a.png)


# BFS(Breadth First Search:너비우선탐색) 알고리즘을 이용하여 문제를 풀이

from collections import deque
# 큐를 이용하기 위해 import

def solution(n, edge):
    answer = 0
    return answer

def bfs (hi, tango, num):
    if hi in tango:
        return num


n       = 6
edge    = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
answer  = 0

graph   = []

for _ in range(n):
    graph.append([])

for n in range(1, n+1):
    for x, y in edge:
        if x == n:
            graph[n-1].append(y)
        if y == n:
            graph[n-1].append(x)

print(graph, '\n')

for i in range(2, len(graph)+1):
    print(i)

graph.remove(graph[0])
while len(graph) != 0:
    temp = graph.pop()

