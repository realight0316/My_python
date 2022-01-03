# 백준 : 숨바꼭질 (https://www.acmicpc.net/problem/1697)

# 문제
# 수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 
# 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 수빈이는 걷거나 순간이동을 할 수 있다. 
# 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 
# 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

# 수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.

# 입력
# 첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.

# 출력
# 수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.

# 예제 입력 -> 4
# 5 17
# 5-10-9-18-17 순으로 가면 4초만에 동생을 찾을 수 있다.

import sys
from collections import deque

def bfs(N, K):                          # BFS 알고리즘
    queue = deque([N])
    while queue:
        x = queue.popleft()
        if x == K:                      # K 지점 도착시 bfs함수 종료
            print(level[x])
            break
        for i in (x+1, x-1, x*2):       # 이동방식 3가지 시도
            if 0 <= i <= 100000 and not level[i]:   # 숫자범위이내, 미방문 숫자인지 확인
                queue.append(i)
                level[i] = level[x] + 1             # 몇단계를 거쳐 도달했는지 기록


start, end = map(int, sys.stdin.readline().split())
level  = [0] * (100001)                 # 단계 기록용

if start > end:                         # 뒤로 가는 경우는 n-1뿐이므로
    answer = start - end                # 시작지점이 더 큰 숫자인 경우를 먼저 계산해서 처리
    print(answer)
    exit()

bfs(start, end)                         # BFS함수 실행
