# 프로그래머스 : [1차] 추석 트래픽 (https://programmers.co.kr/learn/courses/30/lessons/17676)

#입력 형식
# solution 함수에 전달되는 lines 배열은 N(1 ≦ N ≦ 2,000)개의 로그 문자열로 되어 있으며, 
# 각 로그 문자열마다 요청에 대한 응답완료시간 S와 처리시간 T가 공백으로 구분되어 있다.
# 응답완료시간 S는 작년 추석인 2016년 9월 15일만 포함하여 고정 길이 2016-09-15 hh:mm:ss.sss 형식으로 되어 있다.
# 처리시간 T는 0.1s, 0.312s, 2s 와 같이 최대 소수점 셋째 자리까지 기록하며 뒤에는 초 단위를 의미하는 s로 끝난다.
# 예를 들어, 로그 문자열 2016-09-15 03:10:33.020 0.011s은 
# "2016년 9월 15일 오전 3시 10분 33.010초"부터 "2016년 9월 15일 오전 3시 10분 33.020초"까지 "0.011초" 동안 
# 처리된 요청을 의미한다. (처리시간은 시작시간과 끝시간을 포함)
# 서버에는 타임아웃이 3초로 적용되어 있기 때문에 처리시간은 0.001 ≦ T ≦ 3.000이다.
# lines 배열은 응답완료시간 S를 기준으로 오름차순 정렬되어 있다.

# 출력 형식
# solution 함수에서는 로그 데이터 lines 배열에 대해 초당 최대 처리량을 리턴한다.

# line = [
# "2016-09-15 01:00:04.001 2.0s",
# "2016-09-15 01:00:07.000 2s"
# ]
# answer = 1

# line = [
# "2016-09-15 01:00:04.002 2.0s",
# "2016-09-15 01:00:07.000 2s"
# ]
# answer = 2

line = [
"2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"
]
answer = 7

def in_sec(times):      # 입력시간대 밀리세컨드로 변환
    sec = 0
    sec += int(times[:2]) * 3600
    sec += int(times[3:5]) * 60
    sec += int(times[6:8])
    return (sec * 1000) + int(times[9:12])

def solution(lines):
    answer = 0

    secline = []        # 밀리세컨드 기준 로그 [시작시점, 종료시점] 리스트
    for log in lines:
        ss = in_sec(log[11:])
        ms = int(float(log[24:-1]) * 1000) + 1
        start = ss - ms
        end = ss
        secline.append([start, end])

    for x in secline:
        print(x)

    for idx, mslog in enumerate(secline):
        temp = 1
        # print(f"{mslog[0]}, {mslog[1]} // {mslog[1]+999} : {secline[idx][0]}")
    
        while idx < len(lines)-1 and mslog[1]+1000 >= secline[idx+1][0]:
            print(f"{idx}, {mslog} / {(mslog[0])+1000} / {secline[idx+1][0]}")
            temp += 1
            idx += 1
        print()
        answer = max(answer, temp)
        
    return answer

print(in_sec(line[0][11:]))

results = solution(line)
print(f"{answer} / {results}")

# 로그는 자동정렬이니까 내려가면서 하나씩 대조
# 현재값 종료시점이 다음값 시작시점보다 늦으면 +1하고 다음 로그도 대조 (반복)
# / 다음시작보다 빠르면 다음 로그로 이동
# 