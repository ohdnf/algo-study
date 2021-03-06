
# 정답 코드
def compare_two(target, word2):
    for i in range(1, len(target)+1):
        if i == len(target):
            return len(target)
        if target[0:i] != word2[0:i]:
            return i

def compare_three(word1, target, word2):
    for i in range(1, len(target) + 1):
        if i == len(target):
            return len(target)
        if target[0:i] != word1[0:i] and target[0:i] != word2[0:i]:
            return i

    
def solution(words):
    words.sort() 
    answer = 0
    for idx, word in enumerate(words):
        if idx == 0:
            answer += compare_two(words[idx], words[idx+1])
        elif idx == len(words) - 1:
            answer += compare_two(words[idx], words[idx-1])
        else:
            answer += compare_three(words[idx-1], words[idx], words[idx+1])
    return answer



# 시간초과 코드
from collections import defaultdict
def solution(words):
    answer = 0
    words.sort()
    search = defaultdict(int) 
    for word in words:
        temp = ''
        for i in range(0, len(word)):
            temp += word[i]
            search[temp] += 1
    for word in words:
        temp = '' 
        temp_count = 0
        for i in range(0, len(word)):
            temp_count += 1
            temp += word[i]
            if temp == word or search[temp] == 1:
                answer += temp_count
                break 
                
    return answer
