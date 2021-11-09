# 신규아이디 추천 https://programmers.co.kr/learn/courses/30/lessons/72410

# 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
# 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
# 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
# 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
# 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
# 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
#      만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
# 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.


import re
# 정규 표현식 re.sub('패턴', '바꿀문자열', '대상문자열', 바꿀횟수)

def solution(new_id):
    answer = ''

    # 1단계 // 대문자 -> 소문자 치환
    answer = new_id.lower()

    # 2단계 (이중for문 비교법) // 일부 문자빼고 제거
    # tango = 'abcdefghijklmnopqrstuvwxyz123456789-_.'
    # tempstr = ''
    # for i in range(len(answer)):
    #     for j in range(len(tango)):
    #         if answer[i] == tango[j]:
    #             tempstr = tempstr + answer[i]
    # answer = tempstr

    # 2단계 (re.sub 이용) // 일부 문자빼고 제거
    p = re.compile('[^a-z\d\-\_\.]')    # a-z 알파벳, \d 숫자, \- 하이픈, \_ 언더바, \. 점이 아닌것(^)
    answer = p.sub('', answer)          # answer 내용에서 p의 패턴에 해당되는 문자를 ''로 변경

    # 3단계 // 점(.)이 반복되면 하나로 단축
    answer = re.sub('\.{2,}', '.', answer)  # answer에서 점(\.)이 2개이상이면 '.'으로 변환

    # 4단계 // 점(.)이 맨앞에 있거나 맨뒤에 있으면 제거
    answer = re.sub('^\.|\.$', '', answer)  # answer에서 점(\.)이 맨앞(^) 또는(|) 맨뒤($)에 있으면 해당 문자를 ''으로 변환

    # 5단계 // 문자열이 null이면 a 대입
    if answer == '':
        answer = answer + 'a'

    # 6단계 // 문자열 길이가 15자를 초과하면 해당 문자 모두 제거, 맨뒤에 점(.)이 있으면 다시 제거
    answer = re.sub('\.$', '', answer[:15])

    # 7단계 // 2자 이하 아이디는 마지막문자 반복으로 세글자 아이디로 만들어주기
    while len(answer) < 3:
        answer = answer + answer[-1:]   # 문자길이가 3미만이면 answer의 뒤에서 첫번째([-1:])문자 추가를 반복(whlile)

    return answer

new_id = '.ABC...abc-!!!.1234567890'
print('*Input : ' + new_id)
print('*Answer: ' + solution(new_id))