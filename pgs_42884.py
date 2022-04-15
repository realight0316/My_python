# 프로그래머스 : 단속카메라 (https://programmers.co.kr/learn/courses/30/lessons/42884)

# 고속도로를 이동하는 차량의 경로 routes가 매개변수로 주어질 때,
# 모든 차량이 한 번은 단속용 카메라를 만나도록 하려면 
# 최소 몇 대의 카메라를 설치해야 하는지를 return 하도록 solution 함수를 완성하세요.

# 제한사항

# 차량의 대수는 1대 이상 10,000대 이하입니다.
# routes에는 차량의 이동 경로가 포함되어 있으며 routes[i][0]에는 i번째 차량이 고속도로에 진입한 지점,
# routes[i][1]에는 i번째 차량이 고속도로에서 나간 지점이 적혀 있습니다.
# 차량의 진입/진출 지점에 카메라가 설치되어 있어도 카메라를 만난것으로 간주합니다.
# 차량의 진입 지점, 진출 지점은 -30,000 이상 30,000 이하입니다.

# routes= [[-20,-15], [-14,-5], [-18,-13], [-5,-3]]	
# answer= 2
# 입출력 예 설명
# -5 지점에 카메라를 설치하면 두 번째, 네 번째 차량이 카메라를 만납니다.
# -15 지점에 카메라를 설치하면 첫 번째, 세 번째 차량이 카메라를 만납니다.

routes= [[0,2],[2,3],[3,4],[4,6]]
answer= 2

def solution(routes):
    routes = sorted(routes, key=lambda x : x[1])    # 진출시점으로 오름차순 정렬
    print(routes)
    answer = 0
    camera = None                                   # 카메라 위치

    for car in routes:                              # 차량 한대씩 가져와서 하나씩 비교 (그리디알고리즘)
        try:
            if not car[0] <= camera <= car[1]:      # 현재 카메라 위치로 해당 차량을 촬영할 수 없다면
                camera = car[1]                     # 그 차량의 진출시점에 카메라 설치
                answer += 1
        except:                                     # 카메라 최초 위치를 None으로 설정했기 때문에 에러발생, 예외처리
            camera = car[1]                         # 가장 먼저 나가는 차량의 위치는 첫번째 카메라 설치지점
            answer += 1

    return answer

results = solution(routes)
print(f"{answer} / {results}")