# 백준 : 피보나치 함수 (https://www.acmicpc.net/problem/1003)

# 문제
# 다음 소스는 N번째 피보나치 수를 구하는 C++ 함수이다.

# int fibonacci(int n) {
#     if (n == 0) {
#         printf("0");
#         return 0;
#     } else if (n == 1) {
#         printf("1");
#         return 1;
#     } else {
#         return fibonacci(n‐1) + fibonacci(n‐2);
#     }
# }
# fibonacci(3)을 호출하면 다음과 같은 일이 일어난다.

# fibonacci(3)은 fibonacci(2)와 fibonacci(1) (첫 번째 호출)을 호출한다.
# fibonacci(2)는 fibonacci(1) (두 번째 호출)과 fibonacci(0)을 호출한다.
# 두 번째 호출한 fibonacci(1)은 1을 출력하고 1을 리턴한다.
# fibonacci(0)은 0을 출력하고, 0을 리턴한다.
# fibonacci(2)는 fibonacci(1)과 fibonacci(0)의 결과를 얻고, 1을 리턴한다.
# 첫 번째 호출한 fibonacci(1)은 1을 출력하고, 1을 리턴한다.
# fibonacci(3)은 fibonacci(2)와 fibonacci(1)의 결과를 얻고, 2를 리턴한다.
# 1은 2번 출력되고, 0은 1번 출력된다. N이 주어졌을 때, fibonacci(N)을 호출했을 때, 
# 0과 1이 각각 몇 번 출력되는지 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다.

# 각 테스트 케이스는 한 줄로 이루어져 있고, N이 주어진다. N은 40보다 작거나 같은 자연수 또는 0이다.

# 출력
# 각 테스트 케이스마다 0이 출력되는 횟수와 1이 출력되는 횟수를 공백으로 구분해서 출력한다.

# 예제 입력1
# 3
# 0
# 1
# 3
# 예제 출력1
# 1 0
# 0 1
# 1 2

# 예제 입력2
# 2
# 6
# 22
# 예제 출력2
# 5 8
# 10946 17711

# 동적 계획법 (dynamic programming, DP) 
# - 특정 범위까지의 값을 구하기 위해서 그것과 다른 범위까지의 값을 이용하여 효율적으로 값을 구하는 알고리즘 설계 기법이다.

import sys

# 피보나치 수열 : 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597 ...
# N번째 수 = (N-1번째 수) +  (N-2번째 수)
# 수가 X일때 0과 1의 호출횟수도 피보나치 방식으로 증가한다 -> zero[X], one[X]로 표현
zero = [1,0,1]
one  = [0,1,1]

def cal(num):
    if num >= len(zero):                        # 기존 리스트보다 크면 추가로 연산
        for i in range(len(zero), num+1):       # 목표치까지 올라가며 리스트에 추가해준다
            zero.append(zero[i-1]+zero[i-2])    # 0출연횟수 피보나치 방식으로 추가
            one.append(one[i-1]+one[i-2])       # 1출연횟수 피보나치 방식으로 추가
    print(zero[num], one[num])                  # 결과 출력

T = int(sys.stdin.readline())
for _ in range(T):                              # 테스트 케이스
    num = int(sys.stdin.readline())
    cal(num)