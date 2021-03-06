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

