# 프로그래머스 : 전화번호 목록 (https://programmers.co.kr/learn/courses/30/lessons/42577)

# 문제 설명
# 전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다.
# 전화번호가 다음과 같을 경우, 구조대 전화번호는 영석이의 전화번호의 접두사입니다.

# 구조대 : 119
# 박준영 : 97 674 223
# 지영석 : 11 9552 4421
# 전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때, 
# 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return 하도록 solution 함수를 작성해주세요.

# 제한 사항
# phone_book의 길이는 1 이상 1,000,000 이하입니다.
# 각 전화번호의 길이는 1 이상 20 이하입니다.
# 같은 전화번호가 중복해서 들어있지 않습니다.

# phone_book = ["119", "97674223", "1195524421"]
# answer = False

# phone_book = ["123","456","789"]
# answer = True

phone_book = ["12","123","1235","567","88"]
answer = False

def solution2(phone_book):              # 효율성 부족으로 실패처리
    answer = True
    phone_book.sort(key=len)            # 문자 길이순으로 정렬
    for i, num in enumerate(phone_book):
        print(i, num)
        for x in range(i+1, len(phone_book)):       # 현재 문자열과 이후 뒤에 있는 문자열하고 비교하면서 순회
            if num == phone_book[x][:len(num)]:
                return False
    return answer

def solution(phone_book):
    phone_book.sort()                       # 문자열 정렬, 접두어만 확인하는것이라 앞글자기준 정렬만 해도 동일한 문자열끼리 붙여줄 수 있다
    for i, num in enumerate(phone_book):
        if i != len(phone_book)-1 and num == phone_book[i+1][:len(num)]:    # 인덱스 에러방지 and 현재문자와 다음문자가 동일하면 False
            return False
    return True                             # 최종까지 위 조건이 만족되지 않으면 True

def solution_hash(phone_book):      # 문제 분류에 맞게 해시를 이용한 풀이
    hashtable = {}                  # 딕셔너리 {key:value}

    for num in phone_book:          # {전화번호:1}로 구성
        hashtable[num] = 1
    print(hashtable)

    for num in phone_book:          # 해시의 앞부터 순회
        for i in range(len(num)):   # 현재 번호의 앞글자부터 하나씩 늘려가며 비교
            x = num[:i]             # 슬라이싱으로 검색구간 늘리기
            if x in hashtable and x != num:     # 해시테이블에 해당 문자열이 있는지 확인 and 자기 자신 제외
                return False
    return True

result = solution_hash(phone_book)
print(f"{answer} / {result}")