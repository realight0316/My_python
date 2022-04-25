# 프로그래머스 : 자물쇠와 열쇠 (https://programmers.co.kr/learn/courses/30/lessons/60059)

# 표 확장해서 3회 회전하며 비교하고 한칸씩 이동하기

# key	= [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
# lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
# results = True

# key = [[0, 0],[0, 0]]
# lock = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
# results = True

# key = [[1, 1], [1, 1]]
# lock = [[1,1,1],[1,1,1],[1,1,1]]
# results = True

# key = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
# lock = [[1,1,1], [1,1,1], [1,1,1]]
# results = True

# key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
# lock = [[1,2,3],[4,5,6],[7,8,9]]
# results = True

key = [[0, 0],[0, 1]]
lock = [[1, 1], [1, 0]]
results = True

import copy

def rotate (key):       # 회전 기능
    sample = [[0] * len(key) for _ in range(len(key))]      # 회전한 결과를 넣어둘 임시리스트
    for garo in range(len(key)):
        for sero in range(len(key)):
            sample[sero][len(key)-garo-1] = key[garo][sero] # 행렬 90도 회전
    for a in sample:
        print(a)
    return sample

def check (key, extend, garo, sero, lock_len):
    extend2 = copy.deepcopy(extend)                         # 체크함수 내부용 자물쇠리스트 생성
    for kg in range(len(key)):
        for ks in range(len(key)):
            extend2[garo+kg][sero+ks] += key[kg][ks]        # 키와 자물쇠리스트를 합쳐준다
    for lg in range(len(key)-1, len(key)-1+lock_len):
        for ls in range(len(key)-1, len(key)-1+lock_len):
            if extend2[lg][ls] != 1:                        # 0은 채워지지않은 공간, 1은 채워진 공간, 2는 키와 자물쇠가 중복되는 공간
                return False
    return True

def solution(key, lock):
    key_len = len(key)-1
    lock_len = len(lock)
    ex_len = 2*(key_len) + lock_len
    extend = [[0 for a in range(ex_len)] for b in range(ex_len)]    # 자물쇠와 열쇠를 함께 넣을 수 있는 확장리스트

    for idx in range(len(extend)):
        if key_len <= idx < key_len + lock_len:
            for lockpiece in range(len(lock)):
                extend[idx][key_len+lockpiece] = lock[idx-key_len][lockpiece]   # 확장리스트 중앙에 자물쇠 패턴을 삽입

    for garo in range(ex_len - key_len):
        for sero in range(ex_len - key_len):
            for turn in range(5):                                   # 4회 회전하면서 비교할 것임
                if check(key, extend, garo, sero, lock_len):        # 체크함수에서 통과되면 True로 종료
                    for sample in extend:
                        print(sample)
                    return True
                key = rotate(key)                                   # 체크함수를 통과하지 못하면 키 1회 회전


    for sample in extend:
        print(sample)
    return False


answer = solution(key, lock)
print(f"{results} / {answer}")