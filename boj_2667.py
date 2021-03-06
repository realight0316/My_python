# 백준 : 단지번호붙이기 (https://www.acmicpc.net/problem/2667)

# 문제
# <그림 1>과 같이 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다. 
# 철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다. 
# 여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다. 대각선상에 집이 있는 경우는 연결된 것이 아니다. 
# <그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다. 
# 지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.

# 입력
# 첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고, 
# 그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력된다.

# 출력
# 첫 번째 줄에는 총 단지수를 출력하시오. 그리고 각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하시오.

# 예제 입력
# 7
# 0110100
# 0110101
# 1110101
# 0000111
# 0100000
# 0111110
# 0111000

# 예제 출력
# 3
# 7
# 8
# 9

n = int(input())
aptmap = []
answer = list()
for _ in range(n):
    temp = list(map(int, input()))
    aptmap.append(temp)

def bfs(x, y):
    global count        # count 전역변수 선언
    if (x <= -1         # x좌표 0미만 False
        or y <= -1      # y좌표 0미만 False
        or x >= n       # x좌표 n초과 False
        or y >= n):     # y좌표 n초과 False
        return False

    if aptmap[x][y] == 1:
        aptmap[x][y] = 0    # 방문했므로 0으로 변경
        count += 1          # 단지별 건물수 카운트
        bfs(x+1, y)         # 오른쪽으로 이동
        bfs(x-1, y)         # 왼쪽으로 이동
        bfs(x, y+1)         # 위로 이동
        bfs(x, y-1)         # 아래로 이동
        return True
    return False        # 존재하는 좌표지만 건물이 없으면(0) False

count = 0               # count 초기화
for x in range(n):
    for y in range(n):
        if bfs(x, y) == True:   # 시작좌표에 건물이 존재하면 진행
            answer.append(count)# 해당 단지의 건물갯수 정답리스트에 추가
            count = 0           # 단지계산이 종료 되었으므로 재초기화
            
answer.sort()           # 오름차순 정렬
print(len(answer))      # 단지 갯수
for i in answer:        # 단지별 건물갯수 하나씩 출력
    print(i)