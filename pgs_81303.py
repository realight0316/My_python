# 프로그래머스 : 표 편집 (https://programmers.co.kr/learn/courses/30/lessons/81303)

# 문제에 대한 설명은 링크에서 표 그림과 함꼐 이해 필요

# n = 8
# k = 2
# cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]
# answer = "OOOOXOOO"

n = 8
k = 2
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]
answer = "OOXOXOOO"

def solution(n, k, cmd):
    answer = ''
    members = {x:x for x in range(n)}
    origin  = {x:x for x in range(n)}
    now = k
    del_list = []
    print(members)
    for order in cmd:
        if order[0] == 'U':
            now -= int(order[2:])
        elif order[0] == 'D':
            now += int(order[2:])
        elif order[0] == 'C':
            del members[now]
            del_list.append(now)
            if now > len(members):
                now -= 1
        else:
            temp= int(del_list.pop())
            members[temp] = temp

    for idx in range(len(origin)):
        try:
            if members[idx] == origin[idx]:
                answer += "O"
        except:
            answer += 'X'

    return answer

results = solution(n, k, cmd)
print(f"{answer} / {results}")
