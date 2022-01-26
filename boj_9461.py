# 백준 : 파도반 수열 (https://www.acmicpc.net/problem/9461)

# 문제
# 오른쪽 그림과 같이 삼각형이 나선 모양으로 놓여져 있다. 
# 첫 삼각형은 정삼각형으로 변의 길이는 1이다. 그 다음에는 다음과 같은 과정으로 정삼각형을 계속 추가한다.
# 나선에서 가장 긴 변의 길이를 k라 했을 때, 그 변에 길이가 k인 정삼각형을 추가한다.

# 파도반 수열 P(N)은 나선에 있는 정삼각형의 변의 길이이다. 
# P(1)부터 P(10)까지 첫 10개 숫자는 1, 1, 1, 2, 2, 3, 4, 5, 7, 9이다.

# N이 주어졌을 때, P(N)을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, N이 주어진다. 
# (1 ≤ N ≤ 100)

# 출력
# 각 테스트 케이스마다 P(N)을 출력한다.

# 예제 입력
# 2
# 6
# 12
# 예제 출력
# 3
# 16
import sys

DP = [[] for _ in range(101)]               # N 제한만큼 리스트 미리 생성, 0번 슬롯 미사용
DP[1], DP[2], DP[3] = 1, 1, 1               # 1,2,3번 먼저 미리 할당

for _ in range(int(sys.stdin.readline())):  # 테스트 케이스 입력
    N = int(sys.stdin.readline())           # 목표값 입력
    if DP[N] != []:                         # 해당 목표수치의 값을 이미 알고있으면 출력하고 종료
        print(DP[N])
        continue

    for n in range(4, N+1):                 # 해당 목표의 값이 없으므로 연산하여 찾기
        DP[n] = DP[n-2] + DP[n-3]           # 1,1,1,2,2,3,4... 의 규칙에서 볼 수 있듯
    print(DP[N])                            # 해당 n번째의 값은 n-2와n-3번째 값의 합이다.