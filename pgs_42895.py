# 프로그래머스 : N으로 표현 (https://programmers.co.kr/learn/courses/30/lessons/42895)

# 문제 설명
# 아래와 같이 5와 사칙연산만으로 12를 표현할 수 있습니다.

# 12 = 5 + 5 + (5 / 5) + (5 / 5)
# 12 = 55 / 5 + 5 / 5
# 12 = (55 + 5) / 5

# 5를 사용한 횟수는 각각 6,5,4 입니다. 그리고 이중 가장 작은 경우는 4입니다.
# 이처럼 숫자 N과 number가 주어질 때, N과 사칙연산만 사용해서 표현 할 수 있는 방법 중
# N 사용횟수의 최솟값을 return 하도록 solution 함수를 작성하세요.

# 제한사항
# N은 1 이상 9 이하입니다.
# number는 1 이상 32,000 이하입니다.
# 수식에는 괄호와 사칙연산만 가능하며 나누기 연산에서 나머지는 무시합니다.
# 최솟값이 8보다 크면 -1을 return 합니다.

# 입출력 예
# N	number	return
# 5	12	    4
# 2	11	    3

# 입출력 예 설명
# 예제 #1
# 문제에 나온 예와 같습니다.
# 예제 #2
# 11 = 22 / 2와 같이 2를 3번만 사용하여 표현할 수 있습니다.

# 문제풀이 영상 (https://youtu.be/ZsVVTEfZee8)

def solution(N, number):

    if N == number:                         # N과 목표값이 동일하면 바로 종료
        return 1

    setlist = [set() for _ in range(8)]     # set()을 이용하여 요소를 구성 *set(집합자료형): 중복, 순서 없음

    for i in range(8):                      # 숫자를 1~8순으로 사용횟수를 늘려가며 목표값이 나오는지 찾음 
        setlist[i].add(int(str(N)*(i+1)))   # 5, 55, 555, ... 의 단순반복 숫자 먼저 처리, s문자열 처리한 뒤 곱해서 늘려주고 다시 정수형
    
    for i in range(1, 8):                   # 1번 사용하는 것은 N 자기자신뿐이므로 1부터 시작
        for j in range(i):
            for X in setlist[j]:
                for Y in setlist[i-j-1]:
                    setlist[i].add(X+Y)
                    setlist[i].add(X-Y)
                    setlist[i].add(X*Y)
                    if Y != 0:
                        setlist[i].add(X//Y)
        print(setlist)
        if number in setlist[i]:
            return i+1
    return -1
    
# 1번 사용: 5
# 2번 사용:          55                   5+5                      5-5      5*5     5//5
# 3번 사용:      555 55+5 55-5 55*5 55//5 5+5+5 5+5-5 5+5*5 5+5//5 ...
# 4번 사용: 5555 ... 55+5+5 55+5-5 55+5*5 55+5//5
# 패턴이 이전 단계의 요소마다 연산을 한번씩 다 해줘야함
# 곱셈과 나눗셈으로 인해 순서가 바뀌면 연산결과도 달라짐 답을 찾기 위해 모든 경우를 다 연산해야한다
# 숫자 z회 사용시 요소 구성은 z-1회 결과값과 1회 결과값의 연산, z-2는 2, z-3은 3 이런식으로 이루어짐


# N = 5; number =12
N = 2; number =11

print(solution(N, number))