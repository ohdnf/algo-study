def solution(msg):
    answer = []
    
    
    # 1. 길이가 1인 모든 단어 포함토록 사전 초기화
    
    word_dict = {}
    for index in range(26):
        word_dict[chr(ord("A")+index)] = index+1
    next_index = 27
    
    while True:
        
        
        # 2. 사전에서 현재 입력과 일치하는 가장 긴 문자열 w를 찾는다.
        
        end = 0
        while end+1 < len(msg) and msg[:end+2] in word_dict:
            end += 1
        w = msg[:end+1]    
        
        
        # 3. w에 해당하는 사전의 색인 번호를 출력하고, 입력에서 w를 제거한다.
        
        answer.append(word_dict[w])
        msg = msg[end+1:]
        
        
        # 4. 입력에서 처리되지 않은 다음 글자가 남아있다면(c), w+c를 해당하는 단어를 사전에 등록한다.
        
        if msg:
            c = msg[0]
            word_dict[w+c] = next_index
            next_index += 1
        else:
            break
            
    return answer
# 테스트 1 〉	통과 (0.02ms, 10.1MB)
# 테스트 2 〉	통과 (0.03ms, 10.1MB)
# 테스트 3 〉	통과 (0.03ms, 10.2MB)
# 테스트 4 〉	통과 (0.30ms, 10.3MB)
# 테스트 5 〉	통과 (0.04ms, 10.2MB)
# 테스트 6 〉	통과 (0.54ms, 10.2MB)
# 테스트 7 〉	통과 (0.41ms, 10.2MB)
# 테스트 8 〉	통과 (0.47ms, 10.2MB)
# 테스트 9 〉	통과 (0.01ms, 10.1MB)
# 테스트 10 〉	통과 (0.48ms, 10.1MB)
# 테스트 11 〉	통과 (0.31ms, 10.1MB)
# 테스트 12 〉	통과 (0.57ms, 10.2MB)
# 테스트 13 〉	통과 (0.78ms, 10.2MB)
# 테스트 14 〉	통과 (0.78ms, 10.2MB)
# 테스트 15 〉	통과 (0.72ms, 10.2MB)
# 테스트 16 〉	통과 (0.56ms, 10.2MB)
# 테스트 17 〉	통과 (0.47ms, 10.2MB)
# 테스트 18 〉	통과 (0.17ms, 10.1MB)
# 테스트 19 〉	통과 (0.21ms, 10.2MB)
# 테스트 20 〉	통과 (0.45ms, 10.2MB)