# 프로그래머스 : 행렬 테두리 회전하기 (https://programmers.co.kr/learn/courses/30/lessons/77485)

# 문제 설명
# rows x columns 크기인 행렬이 있습니다. 행렬에는 1부터 rows x columns까지의 숫자가 한 줄씩 순서대로 적혀있습니다.
# 이 행렬에서 직사각형 모양의 범위를 여러 번 선택해, 테두리 부분에 있는 숫자들을 시계방향으로 회전시키려 합니다. 각 회전은 (x1, y1, x2, y2)인 정수 4개로 표현하며, 그 의미는 다음과 같습니다.

# x1 행 y1 열부터 x2 행 y2 열까지의 영역에 해당하는 직사각형에서 테두리에 있는 숫자들을 한 칸씩 시계방향으로 회전합니다.
# 다음은 6 x 6 크기 행렬의 예시입니다.
# (https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/ybm/4c3c0fab-11f4-43b6-b290-6f4017e9379f/grid_example.png)

# 이 행렬에 (2, 2, 5, 4) 회전을 적용하면, 아래 그림과 같이 2행 2열부터 5행 4열까지 영역의 테두리가 시계방향으로 회전합니다. 이때, 중앙의 15와 21이 있는 영역은 회전하지 않는 것을 주의하세요.
# (https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/ybm/962df137-5c71-4091-ad9f-8e322910c1ab/rotation_example.png)

# 행렬의 세로 길이(행 개수) rows, 가로 길이(열 개수) columns, 그리고 회전들의 목록 queries가 주어질 때, 각 회전들을 배열에 적용한 뒤, 그 회전에 의해 위치가 바뀐 숫자들 중
# 가장 작은 숫자들을 순서대로 배열에 담아 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# rows는 2 이상 100 이하인 자연수입니다.
# columns는 2 이상 100 이하인 자연수입니다.
# 처음에 행렬에는 가로 방향으로 숫자가 1부터 하나씩 증가하면서 적혀있습니다.
# 즉, 아무 회전도 하지 않았을 때, i 행 j 열에 있는 숫자는 ((i-1) x columns + j)입니다.
# queries의 행의 개수(회전의 개수)는 1 이상 10,000 이하입니다.
# queries의 각 행은 4개의 정수 [x1, y1, x2, y2]입니다.
# x1 행 y1 열부터 x2 행 y2 열까지 영역의 테두리를 시계방향으로 회전한다는 뜻입니다.
# 1 ≤ x1 < x2 ≤ rows, 1 ≤ y1 < y2 ≤ columns입니다.
# 모든 회전은 순서대로 이루어집니다.
# 예를 들어, 두 번째 회전에 대한 답은 첫 번째 회전을 실행한 다음, 그 상태에서 두 번째 회전을 실행했을 때 이동한 숫자 중 최솟값을 구하면 됩니다.

# 입출력 예시
# 6 / 6 / [[2,2,5,4],[3,3,6,6],[5,1,6,3]] / [8, 10, 25]
# 3 / 3	/ [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]	/ [1, 1, 5, 3]
# 100 / 97 / [[1,1,100,97]] / [1]

# (row: 행, column: 열) 행은 가로줄, 열은 세로줄입니다.

def solution(rows, columns, queries):
    answer = []

    # 기본 배열 만들기
    matrix = [[0 for col in range(columns)] for row in range(rows)]
    num = 1
    for x in range(rows):
        for y in range(columns):
            matrix[x][y] = num
            num += 1

    # 입력쿼리 위치 잡기
    for x1, y1, x2, y2 in queries:
        x1 -= 1; y1 -= 1
        x2 -= 1; y2 -= 1                # 문제에서의 좌표는 (1,1)을 시작점으로 하는 행렬이라서 -1을 미리 하여 (0,0)기준 행렬로 만들어줌

                                        # 진행순서는 좌측 -> 하단 -> 우측 -> 상단
        memory = matrix[x1][y1]         # 처음 진행하는 수를 마지막에 써야하기때문에 'memory'에 저장
        mini = memory                   # 최초 숫자는 비교대상이 없으므로 최솟값으로 취급 
        for ll in range(x1, x2):        # left line : 좌측 세로선이기 때문에 변하는 값은 x값만 변화
            temp = matrix[ll+1][y1]
            matrix[ll][y1] = temp       # 가져올 값을 temp에 넣어서 다음으로 이동
            mini = min(mini, temp)      # 가져온 값이 최솟값인지 비교해보고 작은 값을 mini에 대입

        for bl in range(y1, y2):        # bottom line : 위 방식과 동일
            temp = matrix[x2][bl+1]
            matrix[x2][bl] = temp
            mini = min(mini, temp)

        for rl in range(x2, x1, -1):    # right line : 위 방식과 동일
            temp = matrix[rl-1][y2]
            matrix[rl][y2] = temp
            mini = min(mini, temp)

        for tl in range(y2, y1, -1):    # top line : 위 방식과 동일
            temp = matrix[x1][tl-1]
            matrix[x1][tl] = temp
            mini = min(mini, temp)

        matrix[x1][y1+1] = memory       # memory에 넣어둔 최초값을 이동, 회전 완료
        answer.append(mini)             # 회전하면서 비교한 최솟값을 정답에 덧붙이기

    for result in matrix:               # 회전을 완료시킨 행렬 결과 확인해보기
        print(result)
    print()

    return answer

rows    = 6
columns = 6
queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
print(rows, columns, queries, '\n')

print(solution(rows, columns, queries))



