# 백준 체스판 다시 칠하기 (https://www.acmicpc.net/problem/1018)

# 문제
# 지민이는 자신의 저택에서 MN개의 단위 정사각형으로 나누어져 있는 M×N 크기의 보드를 찾았다.
# 어떤 정사각형은 검은색으로 칠해져 있고, 나머지는 흰색으로 칠해져 있다. 지민이는 이 보드를 잘라서 8×8 크기의 체스판으로 만들려고 한다.

# 체스판은 검은색과 흰색이 번갈아서 칠해져 있어야 한다.
# 구체적으로, 각 칸이 검은색과 흰색 중 하나로 색칠되어 있고,
# 변을 공유하는 두 개의 사각형은 다른 색으로 칠해져 있어야 한다.
# 따라서 이 정의를 따르면 체스판을 색칠하는 경우는 두 가지뿐이다.
# 하나는 맨 왼쪽 위 칸이 흰색인 경우, 하나는 검은색인 경우이다.

# 보드가 체스판처럼 칠해져 있다는 보장이 없어서,
# 지민이는 8×8 크기의 체스판으로 잘라낸 후에 몇 개의 정사각형을 다시 칠해야겠다고 생각했다. 당연히 8*8 크기는 아무데서나 골라도 된다.
# 지민이가 다시 칠해야 하는 정사각형의 최소 개수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N과 M이 주어진다. N과 M은 8보다 크거나 같고, 50보다 작거나 같은 자연수이다.
# 둘째 줄부터 N개의 줄에는 보드의 각 행의 상태가 주어진다. B는 검은색이며, W는 흰색이다.

# 출력
# 첫째 줄에 지민이가 다시 칠해야 하는 정사각형 개수의 최솟값을 출력한다.

# 예제 입력     -> 예제 출력 12
# 10 13
# BBBBBBBBWBWBW
# BBBBBBBBBWBWB
# BBBBBBBBWBWBW
# BBBBBBBBBWBWB
# BBBBBBBBWBWBW
# BBBBBBBBBWBWB
# BBBBBBBBWBWBW
# BBBBBBBBBWBWB
# WWWWWWWWWWBWB
# WWWWWWWWWWBWB

n, m = map(int, input().split())
board = []
ans   = []

for _ in range(n):
    board.append(input())

for i in range(n-7):            # 한 지점을 기준으로 8x8을 비교해야함으로
    for j in range(m-7):        # 전체 길이에서 7을 빼줌, 만약 보드자체가 8x8인데 8을 빼면 보드가 사라짐
        W_start = 0             # W로 시작하는 보드일때 바뀌는 칸의 수
        B_start = 0             # B로 시작하는 보드일때 바뀌는 칸의 수

        # 이해 예시 
        # WBWBWBWB 
        # BWBWBWBW
        # 위 보드에서 W는 (0,0), (0,2), ... (1,1), (1,3), ... 의 규칙을 가짐
        # 즉 x + y가 짝수인 좌표타일의 색은 시작하는 타일의 색과 같다

        for x in range(i, i+8):             # 시작지점으로 부터 8칸까지
            for y in range(j, j+8):
                if (x+y) % 2 == 0:          # 위 조건에 따라 짝수인 경우
                    if board[x][y] != 'W':  # W가 아니면
                        W_start += 1        # W시작보드에선 바뀌어야 함으로 +1
                    if board[x][y] != 'B':
                        B_start += 1
                else:                       # 짝수가 아닐때
                    if board[x][y] != 'B':  # B가 아니면
                        W_start += 1        # W시작보드에선 바뀌어야 함으로 +1
                    if board[x][y] != 'W':
                        B_start += 1

        ans.append(min(W_start, B_start))   # 할당된 보드에서 W와 B중에서 최소 타일변화수를 ans에 모음
    
print(min(ans))                             # 모든 비교가 종료되면 지금까지의 ans중에서 최소변화수를 정답으로 출력