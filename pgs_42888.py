# 프로그래머스 : 오픈채팅방 (https://programmers.co.kr/learn/courses/30/lessons/42888)

# 제한사항
# record는 다음과 같은 문자열이 담긴 배열이며, 길이는 1 이상 100,000 이하이다.
# 다음은 record에 담긴 문자열에 대한 설명이다.
# 모든 유저는 [유저 아이디]로 구분한다.
# [유저 아이디] 사용자가 [닉네임]으로 채팅방에 입장 - "Enter [유저 아이디] [닉네임]" (ex. "Enter uid1234 Muzi")
# [유저 아이디] 사용자가 채팅방에서 퇴장 - "Leave [유저 아이디]" (ex. "Leave uid1234")
# [유저 아이디] 사용자가 닉네임을 [닉네임]으로 변경 - "Change [유저 아이디] [닉네임]" (ex. "Change uid1234 Muzi")
# 첫 단어는 Enter, Leave, Change 중 하나이다.
# 각 단어는 공백으로 구분되어 있으며, 알파벳 대문자, 소문자, 숫자로만 이루어져있다.
# 유저 아이디와 닉네임은 알파벳 대문자, 소문자를 구별한다.
# 유저 아이디와 닉네임의 길이는 1 이상 10 이하이다.
# 채팅방에서 나간 유저가 닉네임을 변경하는 등 잘못 된 입력은 주어지지 않는다.

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
answer = ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]

def solution(record):
    answer = []
    users = {}                  # users = {유저 아이디 : 닉네임} 딕셔너리
    logs = []                   # 출입 기록 리스트

    for rec in record:
        if rec[0] == 'E':                       # 입장
            temp = list(map(str, rec.split()))  # 기록 분해해서
            users[temp[1]] = temp[2]            # 유저아이디, 닉네임 확인
            logs.append([temp[0], temp[1]])     # 입장, 유저아이디 저장
        elif rec[0] == 'L':                     # 퇴장
            temp = list(map(str, rec.split()))  # 기록 분해해서
            logs.append([temp[0], temp[1]])     # 퇴장, 유저아이디 저장
        else:                                   # 닉네임 변경
            temp = list(map(str, rec.split()))  # 기록 분해해서
            users[temp[1]] = temp[2]            # 해당 유저아이디 닉네임 변경

    print(users)
    print(logs)

    for log in logs:                            # 로그에 따라서
        if log[0] == 'Enter':                   # 입장 시
            answer.append(f"{users[log[1]]}님이 들어왔습니다.") # 딕셔너리에서 닉네임 가져오기
        else:                                   # 퇴장 시
            answer.append(f"{users[log[1]]}님이 나갔습니다.")   # 딕셔너리에서 닉네임 가져오기 
    return answer

results = solution(record)
print(f"{answer} / {results}")