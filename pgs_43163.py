# 프로그래머스 : 단어 변환 (https://programmers.co.kr/learn/courses/30/lessons/43163)

# 문제 설명
# 두 개의 단어 begin, target과 단어의 집합 words가 있습니다. 
# 아래와 같은 규칙을 이용하여 begin에서 target으로 변환하는 가장 짧은 변환 과정을 찾으려고 합니다.

# 1. 한 번에 한 개의 알파벳만 바꿀 수 있습니다.
# 2. words에 있는 단어로만 변환할 수 있습니다.
# 예를 들어 begin이 "hit", target가 "cog", words가 ["hot","dot","dog","lot","log","cog"]라면 
# "hit" -> "hot" -> "dot" -> "dog" -> "cog"와 같이 4단계를 거쳐 변환할 수 있습니다.

# 두 개의 단어 begin, target과 단어의 집합 words가 매개변수로 주어질 때, 
# 최소 몇 단계의 과정을 거쳐 begin을 target으로 변환할 수 있는지 return 하도록 solution 함수를 작성해주세요.

# 제한사항
# 각 단어는 알파벳 소문자로만 이루어져 있습니다.
# 각 단어의 길이는 3 이상 10 이하이며 모든 단어의 길이는 같습니다.
# words에는 3개 이상 50개 이하의 단어가 있으며 중복되는 단어는 없습니다.
# begin과 target은 같지 않습니다.
# 변환할 수 없는 경우에는 0를 return 합니다.

begin= "hit"
target= "cog"
words= ["hot", "dot", "dog", "lot", "log", "cog"]
answer= 4

# begin= "hit"
# target= "cog"
# words= ["hot", "dot", "dog", "lot", "log"]
# answer= 0
# target인 "cog"는 words 안에 없기 때문에 변환할 수 없습니다.

def solution(begin, target, words):
    if target not in words:     # 목표단어가 없으면 변환 불가능
        return 0
    answer = 0
    word_list = [begin]         # 변경 단어 저장, 첫 스타트는 시작 단어

    while True:
        for wl in word_list:    # 변경할 단어 가져오기
            diff_word = []      # 단어 변경 과정
            for word in words:
                diff = 0        # 다른 알파벳 갯수
                for idx in range (len(begin)):  # 알파벳 하나씩 비교하기 위한 인덱스
                    if wl[idx] != word[idx]:    # 현재 단어 한글자와 비교할 단어의 한글자가 다르면
                        diff += 1               # 다른 알파벳 갯수 1 추가
                    if diff > 1:                # 다른 알파벳 갯수가 2개 이상이면 비교 중지
                        break
                if diff == 1:                   # 다른 알파벳 갯수가 하나면
                    diff_word.append(word)      # 그 단어를 변경과정에 추가
                    words.remove(word)          # 그리고 원래있던 리스트에서 제거
        
        answer += 1                             # 한단계 거쳤으므로 +1
        if target in diff_word: return answer   # 목표단어가 변경과정에 들어오면 종료
        else: word_list = diff_word             # 없으면 변경된 단어로 재실행
            

result= solution(begin, target, words)
print(f"{answer} / {result}")