# 프로그래머스 : 뉴스 클러스터링 (https://programmers.co.kr/learn/courses/30/lessons/17677)

# 자카드 유사도는 집합 간의 유사도를 검사하는 여러 방법 중의 하나로 알려져 있다. 
# 두 집합 A, B 사이의 자카드 유사도 J(A, B)는 두 집합의 교집합 크기를 두 집합의 합집합 크기로 나눈 값으로 정의된다.

# 예를 들어 집합 A = {1, 2, 3}, 집합 B = {2, 3, 4}라고 할 때, 교집합 A ∩ B = {2, 3}, 합집합 A ∪ B = {1, 2, 3, 4}이 되므로, 
# 집합 A, B 사이의 자카드 유사도 J(A, B) = 2/4 = 0.5가 된다. 
# 집합 A와 집합 B가 모두 공집합일 경우에는 나눗셈이 정의되지 않으니 따로 J(A, B) = 1로 정의한다.

# 자카드 유사도는 원소의 중복을 허용하는 다중집합에 대해서 확장할 수 있다. 다중집합 A는 원소 "1"을 3개 가지고 있고, 
# 다중집합 B는 원소 "1"을 5개 가지고 있다고 하자. 
# 이 다중집합의 교집합 A ∩ B는 원소 "1"을 min(3, 5)인 3개, 합집합 A ∪ B는 원소 "1"을 max(3, 5)인 5개 가지게 된다. 
# 다중집합 A = {1, 1, 2, 2, 3}, 다중집합 B = {1, 2, 2, 4, 5}라고 하면, 교집합 A ∩ B = {1, 2, 2}, 합집합 A ∪ B = {1, 1, 2, 2, 3, 4, 5}가 되므로, 
# 자카드 유사도 J(A, B) = 3/7, 약 0.42가 된다.

# 이를 이용하여 문자열 사이의 유사도를 계산하는데 이용할 수 있다. 문자열 "FRANCE"와 "FRENCH"가 주어졌을 때, 
# 이를 두 글자씩 끊어서 다중집합을 만들 수 있다. 
# 각각 {FR, RA, AN, NC, CE}, {FR, RE, EN, NC, CH}가 되며, 교집합은 {FR, NC}, 합집합은 {FR, RA, AN, NC, CE, RE, EN, CH}가 되므로, 
# 두 문자열 사이의 자카드 유사도 J("FRANCE", "FRENCH") = 2/8 = 0.25가 된다.

# 입력 형식
# 입력으로는 str1과 str2의 두 문자열이 들어온다. 각 문자열의 길이는 2 이상, 1,000 이하이다.
# 입력으로 들어온 문자열은 두 글자씩 끊어서 다중집합의 원소로 만든다. 이때 영문자로 된 글자 쌍만 유효하고, 
# 기타 공백이나 숫자, 특수 문자가 들어있는 경우는 그 글자 쌍을 버린다. 예를 들어 "ab+"가 입력으로 들어오면, "ab"만 다중집합의 원소로 삼고, "b+"는 버린다.
# 다중집합 원소 사이를 비교할 때, 대문자와 소문자의 차이는 무시한다. "AB"와 "Ab", "ab"는 같은 원소로 취급한다.

# 출력 형식
# 입력으로 들어온 두 문자열의 자카드 유사도를 출력한다. 유사도 값은 0에서 1 사이의 실수이므로, 이를 다루기 쉽도록 65536을 곱한 후에 소수점 아래를 버리고 정수부만 출력한다.

str1= 'FRANCE'
str2= 'french'
answer= 16384

# str1= 'handshake'
# str2= 'shake hands'
# answer= 65536

# str1= 'aa1+aa2'
# str2= 'AAAA12'
# answer= 43690

# str1= 'E=M*C^2'
# str2= 'e=m*c^2'
# answer= 65536

from typing import Counter

def solution(str1, str2):
    parts1, parts2 = [], []                 # 문자열을 각각 위 조건에 맞는 다중 집합으로 만들 리스트 두개

    for i in range(len(str1)-1):            # 문자열 맨앞부터 뒤에서 두번째까지 순회
        p = (str1[i]+str1[i+1]).upper()     # p = 현재문자 + 다음문자
        if p.isalpha():                     # p가 문자로만 이루어져있으면
            parts1.append(p)                # 집합에 추가해서 가져간다
        
    for i in range(len(str2)-1):            # 위와 동일
        p = (str2[i]+str2[i+1]).upper()
        if p.isalpha():
            parts2.append(p)

    c1 = Counter(parts1)                    # 다중 집합의 원소별로 몇개 있는지 확인(원소는 중복이 있을 수 있음, 딕셔너리 출력)
    c2 = Counter(parts2)

    print(c1 &c2)
    print(c1 | c2)

    denominator = sum((c1 | c2).values())   # 두 딕셔너리의 교집합을 구하고 요소들의 값을 모두 더하기 (denominator: 분모)
    numerator = sum((c1 & c2).values())     # (numerator: 분자)

    print(numerator)
    print(denominator)

    if numerator == denominator == 0:       # 교집합과 합집합이 공집합이면
        return 65536                        # 유사도는 1로 취급한다

    return int((numerator/denominator)*65536)

result = solution(str1, str2)
print(f"{answer} / {result}")
