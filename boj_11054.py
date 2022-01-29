# 백준 : 가장 긴 바이토닉 부분 수열 (https://www.acmicpc.net/problem/11054)

# 문제
# 수열 S가 어떤 수 Sk를 기준으로 S1 < S2 < ... Sk-1 < Sk > Sk+1 > ... SN-1 > SN을 만족한다면, 
# 그 수열을 바이토닉 수열이라고 한다.

# 예를 들어, {10, 20, 30*, 25, 20}과 {10, 20, 30, 40*}, {50*, 40, 25, 10} 은 바이토닉 수열이지만,  
# {1, 2, 3, 2, 1, 2, 3, 2, 1}과 {10, 20, 30, 40, 20, 30} 은 바이토닉 수열이 아니다.

# 수열 A가 주어졌을 때, 그 수열의 부분 수열 중 바이토닉 수열이면서 가장 긴 수열의 길이를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 수열 A의 크기 N이 주어지고, 둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ N ≤ 1,000, 1 ≤ Ai ≤ 1,000)

# 출력
# 첫째 줄에 수열 A의 부분 수열 중에서 가장 긴 바이토닉 수열의 길이를 출력한다.

# 예제 입력1 -> 7
# 10
# 1 5 2 1 4 3 4 5 2 1
# 힌트
# 예제의 경우 {1 5 2 1 4 3 4 5* 2 1}이 가장 긴 바이토닉 부분 수열이다.

import sys
n = int(sys.stdin.readline())
progression = list(map(int, sys.stdin.readline().split()))
re_progression = list(reversed(progression))                # 주어진 수열과, 뒤집은 수열 두가지를 사용
dp1 = [1 for _ in range(n)]                                 # 해당값까지 몇단계 상승인지 저장
dp2 = [1 for _ in range(n)]                                 # 역순으로 내려올때 몇단계 상승인지 저장
answer = 0

for i in range(n):
    for j in range(i):
        if progression[i] > progression[j]:                 # 증가하는 수열이므로 클때만 확인
            dp1[i] = max(dp1[i], dp1[j]+1)                  # 현재값의 단계와 비교단계가 가진 단계 중 큰 값으로 갱신
        if re_progression[i] > re_progression[j]:           # 리스트를 역순으로 뒤집어서 위와 동일한 진행
            dp2[i] = max(dp2[i], dp2[j]+1)

dp2 = list(reversed(dp2))                                   # 역순리스트로 정답을 기록했으므로 다시 뒤집기
for x, y in zip(dp1, dp2):                                  # dp1 : 해당값으로 올라오는 횟수 / dp2 : 내려오면서 해당값으로 내려오는 횟수
    answer = max(answer, x+y-1)                             # 가장 긴 수열길이만 알면 되므로 max 사용, 
                                                            # 상승일때 한번, 하강일때 한번, 즉 자신이 2번 카운팅 되므로 -1

print(answer)
