# 프로그래머스 : 순위 (https://programmers.co.kr/learn/courses/30/lessons/49191)

#문제 설명
# n명의 권투선수가 권투 대회에 참여했고 각각 1번부터 n번까지 번호를 받았습니다. 
# 권투 경기는 1대1 방식으로 진행이 되고, 만약 A 선수가 B 선수보다 실력이 좋다면 A 선수는 B 선수를 항상 이깁니다. 
# 심판은 주어진 경기 결과를 가지고 선수들의 순위를 매기려 합니다. 
# 하지만 몇몇 경기 결과를 분실하여 정확하게 순위를 매길 수 없습니다.

# 선수의 수 n, 경기 결과를 담은 2차원 배열 results가 매개변수로 주어질 때 
# 정확하게 순위를 매길 수 있는 선수의 수를 return 하도록 solution 함수를 작성해주세요.

# 제한사항
# 선수의 수는 1명 이상 100명 이하입니다.
# 경기 결과는 1개 이상 4,500개 이하입니다.
# results 배열 각 행 [A, B]는 A 선수가 B 선수를 이겼다는 의미입니다.
# 모든 경기 결과에는 모순이 없습니다.

n= 5
results= [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
answer= 2

def solution(n, results):
    answer = 0
    wins = [set() for _ in range(n+1)]  # 중복방지를 위해 set 사용, 0번째는 미사용
    loses= [set() for _ in range(n+1)]

    for x, y in results:                # results 승자별, 패자별 정리
        wins[x].add(y)                  # x는 y에게 승리했다
        loses[y].add(x)                 # y는 x에게 패배했다

    for idx in range(1, n+1):
        for a in wins[idx]:
            loses[a].update(loses[idx])    # idx는 a를 이긴다, idx를 이기면 a도 이긴다.
        for b in loses[idx]:
            wins[b].update(wins[idx])      # idx는 b에게 진다, idx에게 지면 b에게도 진다.

    for m in range(n+1):                   # 경기기록이 n-1개면 판단가능
        if len(wins[m]) + len(loses[m]) == n-1:
            answer += 1

    print("승리:", wins)
    print("패배:", loses)
    return answer

myresult= solution(n, results)
print("{} / {}".format(answer, myresult))