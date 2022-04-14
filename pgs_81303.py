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

class node:                 # 연결리스트로 노드구성
    def __init__(self):
        self.remv = False   # 제거여부
        self.prev = None    # 이전 노드 지정
        self.next = None    # 다음 노드 지정

def solution2(n, k, cmd):
    answer = ''
    members = [node() for _ in range(n)]    # 위에서 만든 노드구조로 연결리스트 생성
    now = members[k]                        # 현재 노드
    del_list = []                           # 제거된 노드 스택

    for i in range(1, n):                   # 첫번째와 마지막 노드는 각각 이전/다음 노드가 없으므로 1~n-1까지
        members[i-1].next = members[i]      # 다음 노드의 이전 노드는 현재 노드
        members[i].prev = members[i-1]      # 이전 노드의 다음 노드는 현재 노드
    
    for order in cmd:
        if order[0] == 'U':
            for _ in range(int(order[2:])):
                now = now.prev              # 이전 노드 타고 이동
        elif order[0] == 'D':
            for _ in range(int(order[2:])):
                now = now.next              # 다음 노드 타고 이동
        elif order[0] == 'C':
            now.remv = True                 # 삭제 처리
            del_list.append(now)            # 삭제된 노드정보를 스택 저장
            if now.prev:                    # 이전노드가 존재하면
                (now.prev).next = now.next  # 이전노드와 다음노드를 연결
            if now.next:                    # 다음노드가 존재하면
                (now.next).prev = now.prev  # 다음노드와 이전노드를 연결
                now = now.next              # 다음노드를 현재 노드로 지정
            else:
                now = now.prev              # 다음노드가 존재하지 않으면 이전노드가 현재노드
        else:
            temp = del_list.pop()           # 제거스택 LIFO 나중에 들어간게 먼저 나옴
            temp.remv = False               # 복구 처리
            up = temp.prev
            down = temp.next
            if up:
                up.next = temp              # 이전 노드와 현재노드 연결
            if down:
                down.prev = temp            # 현재 노드와 이전노드 연결
    
    for i in range(n):
        if members[i].remv:                 # 제거처리된 노드를 X
            answer += 'X'
        else:
            answer += 'O'


    return answer

results = solution2(n, k, cmd)
print(f"{answer} / {results}")
