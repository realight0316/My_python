# 백준 : 팩토리얼 (https://www.acmicpc.net/problem/10872)

# 문제
# 0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 정수 N(0 ≤ N ≤ 12)이 주어진다.

# 출력
# 첫째 줄에 N!을 출력한다.

# 예제 입력1: 10 -> 출력: 3628800
# 예제 입력2: 0  -> 출력: 1

def recursive_function(n):              # recursive : 반복되는
    if n <= 1:
        return 1                        # n이 0이거나 1이면 1리턴, 순환종료
    return n * recursive_function(n-1)  # 팩토리얼식에 함수 대입하여 재귀함수화

num = int(input())

print(recursive_function(num))
