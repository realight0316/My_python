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

def solution2(phone_book):      # 효율성 부족으로 실패처리
    answer = True
    phone_book.sort(key=len)
    for i, num in enumerate(phone_book):
        print(i, num)
        for x in range(i+1, len(phone_book)):
            if num == phone_book[x][:len(num)]:
                print("if:", phone_book[x][:len(num)])
                return False
    return answer

def solution(phone_book):
    phone_book.sort()
    for i, num in enumerate(phone_book):
        if i != len(phone_book)-1 and num == phone_book[i+1][:len(num)]:
            return False
    return True

def solution_hash(phone_book):      # 문제 분류에 맞게 해시를 이용한 풀이
    hashtable = {}

    for num in phone_book:
        hashtable[num] = 1
    print(hashtable)

    for num in phone_book:
        for i in range(len(num)):
            x = num[:i]
            if x in phone_book:
                return False
    return True

result = solution_hash(phone_book)
print(f"{answer} / {result}")