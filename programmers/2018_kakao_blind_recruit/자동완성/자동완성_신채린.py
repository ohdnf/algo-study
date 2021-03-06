
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

'''
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.4MB)
테스트 3 〉	통과 (0.02ms, 10.3MB)
테스트 4 〉	통과 (0.02ms, 10.2MB)
테스트 5 〉	통과 (0.02ms, 10.2MB)
테스트 6 〉	통과 (192.14ms, 17.9MB)
테스트 7 〉	통과 (0.02ms, 10.3MB)
테스트 8 〉	통과 (190.21ms, 18.1MB)
테스트 9 〉	통과 (0.02ms, 10.2MB)
테스트 10 〉	통과 (0.02ms, 10.3MB)
테스트 11 〉	통과 (0.02ms, 10.2MB)
테스트 12 〉	통과 (204.16ms, 17.9MB)
테스트 13 〉	통과 (196.71ms, 17.9MB)
테스트 14 〉	통과 (0.14ms, 12MB)
테스트 15 〉	통과 (0.01ms, 10.3MB)
테스트 16 〉	통과 (202.64ms, 17.8MB)
테스트 17 〉	통과 (193.83ms, 17.8MB)
테스트 18 〉	통과 (0.02ms, 10.3MB)
테스트 19 〉	통과 (0.16ms, 11.9MB)
테스트 20 〉	통과 (185.50ms, 17.8MB)
테스트 21 〉	통과 (0.16ms, 12MB)
테스트 22 〉	통과 (0.03ms, 11.8MB)
'''



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
