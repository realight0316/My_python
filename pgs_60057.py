# 프로그래머스 : 문자열 압축 (https://programmers.co.kr/learn/courses/30/lessons/60057)

# s= "aabbaccc"
# result= 7

# s= "ababcdcdababcdcd"
# result= 9

# s= "abcabcdede"
# result= 8

# s= "abcabcabcabcdededededede"
# result= 14

s= "xababcdcdababcdcd"
result= 17

import math

def solution(s):
    max_lens= len(s)
    answer= max_lens
    for n in range(1, math.ceil(max_lens/2)+1):     # 절반길이(max_lens/2)까지만 확인, 그 이상은 압축의 의미가 없음
                                                    # 길이가 홀수일 경우 올림(math.ceil)하여 한번 더 시도
                                                    # [ex. 길이 7일 경우 올림처리 3이 되어 3, 3, 1로 압축시도를 할 수 있음]
        splitlist= []
        slicing= max_lens//n                        # 현재 할당 길이로 몇번 나누어 지는지 확인
        for s_n in range(slicing):
            splitlist.append(s[s_n*n:s_n*n+n])      # 할당 길이로 나눈 슬라이싱을 splitlist에 따로 모음
            if s_n == slicing-1:
                splitlist.append(s[s_n*n+n:])       # 할당 길이 이하의 남은 문자까지 추가 정리
        print(n, splitlist)
        cnt= 1
        ex_answer= ""
        for idx, unit in enumerate(splitlist):      # 슬라이싱 한개(unit)와 순번(idx) 할당
            if idx == 0: continue                   # 현 유닛과 앞의 유닛을 비교하는 방식이므로 첫번째는 스킵
            if unit == splitlist[idx-1]:            # 현 유닛과 앞 유닛이 동일할 경우 카운트(cnt)+1
                cnt+= 1
            elif cnt!= 1:                           # 다른 유닛인데 카운트가 2개 이상일 경우 숫자와 함께 기록
                ex_answer += str(cnt) + splitlist[idx-1]
                cnt= 1                              # 카운트 초기화
            else:
                ex_answer += splitlist[idx-1]       # 유닛이 하나면 숫자는 미기입

            if idx == len(splitlist)-1:             # 마지막 유닛 처리
                if cnt==1:                          # 한개의 유닛은 숫자 미기입
                    ex_answer += unit
                else:
                    ex_answer += str(cnt) + unit    # 두개이상은 숫자와 함께 기입
                print(
                    """
                    한 세션 종료
                    answer: {}
                    ex_answer: {} / {}
                    """.format(answer, len(ex_answer), ex_answer))
                answer = min(answer, len(ex_answer))

            # print(idx, unit)
            # print("{} / {}".format(cnt, ex_answer))
    print(answer)
    return answer



answer= solution(s)
print("결과:", answer)
print("정답:", result)

splitlist2= list(map(''.join, zip(*[iter(s)]*2)))    # 단위별 분할시 쓴 명령어인데 잔여문자 처리가 안되서 미사용