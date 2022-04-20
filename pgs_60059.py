# 프로그래머스 : 자물쇠와 열쇠 (https://programmers.co.kr/learn/courses/30/lessons/60059)

# 표 확장해서 3회 회전하며 비교하고 한칸씩 이동하기

key	= [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
results = True

def solution(key, lock):
    key_len = len(key)-1
    lock_len = len(lock)
    ex_len = 2*(key_len) + lock_len
    extend = [[0 for a in range(ex_len)] for b in range(ex_len)]

    for idx in range(len(extend)):
        if key_len <= idx <= key_len + key_len:
            for lockpiece in range(len(lock)):
                extend[idx][key_len+lockpiece] = lock[key_len-idx][lockpiece]

    for sample in extend:
        print(sample)
    return False

answer = solution(key, lock)
print(f"{results} / {answer}")