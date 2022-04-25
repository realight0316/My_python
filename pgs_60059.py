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

def rotate (key):
    sample = [[0 for _ in range(len(key))] for _ in range(len(key))]
    for garo in range(len(key)):
        for sero in range(len(key)):
            sample[sero][len(key)-garo-1] = key[garo][sero]
            for a in sample:
                print(a)
            print()
    return sample

def check (key, extend, garo, sero, lock_len):
    extend2 = copy.deepcopy(extend)
    for kg in range(len(key)):
        for ks in range(len(key)):
            extend2[garo+kg][sero+kg] += key[kg][ks]
    for lg in range(len(key)-1, len(key)-1+lock_len):
        for ls in range(len(key)-1, len(key)-1+lock_len):
            if extend2[lg][ls] != 1:
                return False
    return True

def solution(key, lock):
    key_len = len(key)-1
    lock_len = len(lock)
    ex_len = 2*(key_len) + lock_len
    extend = [[0 for a in range(ex_len)] for b in range(ex_len)]

    for idx in range(len(extend)):
        if key_len <= idx < key_len + lock_len:
            for lockpiece in range(len(lock)):
                extend[idx][key_len+lockpiece] = lock[idx-key_len][lockpiece]

    for garo in range(ex_len - key_len):
        for sero in range(ex_len - key_len):
            for turn in range(5):
                if check(key, extend, garo, sero, lock_len):
                    for sample in extend:
                        print(sample)
                    return True
                key = rotate(key)

    for sample in extend:
        print(sample)
    return False

answer = solution(key, lock)
print(f"{results} / {answer}")