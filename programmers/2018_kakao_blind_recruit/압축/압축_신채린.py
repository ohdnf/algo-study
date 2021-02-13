def solution(msg):
    dic = dict() 
    lst = []
    [lst.append(chr(i)) for i in range(ord('A'), ord('Z') + 1)]
    for idx, alphabet in enumerate(lst):
        dic[alphabet] = idx + 1
        
    lastIdx = 26
    idx = 0
    length = 0
    answer = [] 
    
    while True:
        length += 1
        # 현재 글자가 사전에 없는 경우 
        if not msg[idx:idx+length] in dic:
            # answer에 이전글자까지 색인 번호 출력 
            answer.append(dic[msg[idx:idx+length-1]])
            # 사전에 등록한다 
            lastIdx += 1
            dic[msg[idx:idx+length]] = lastIdx
            # idx를 다음으로 옮겨간다.
            idx += length -1 
            length = 0
        else:
            # 마지막으로 처리되지 않은 글자를 출력
            if idx + length - 1 == len(msg):
                answer.append(dic[msg[idx:idx+length-1]])
                break
    return answer

# 테스트 1 〉	통과 (0.02ms, 10.2MB)
# 테스트 2 〉	통과 (0.03ms, 10.1MB)
# 테스트 3 〉	통과 (0.02ms, 10.1MB)
# 테스트 4 〉	통과 (0.37ms, 10.3MB)
# 테스트 5 〉	통과 (0.05ms, 10.2MB)
# 테스트 6 〉	통과 (0.64ms, 10.2MB)
# 테스트 7 〉	통과 (0.46ms, 10.2MB)
# 테스트 8 〉	통과 (0.55ms, 10.2MB)
# 테스트 9 〉	통과 (0.02ms, 10.1MB)
# 테스트 10 〉	통과 (0.53ms, 10.3MB)
# 테스트 11 〉	통과 (0.37ms, 10.2MB)
# 테스트 12 〉	통과 (0.65ms, 10.2MB)
# 테스트 13 〉	통과 (0.97ms, 10.2MB)
# 테스트 14 〉	통과 (0.95ms, 10.3MB)
# 테스트 15 〉	통과 (0.50ms, 10.3MB)
# 테스트 16 〉	통과 (0.76ms, 10.2MB)
# 테스트 17 〉	통과 (0.68ms, 10.2MB)
# 테스트 18 〉	통과 (0.20ms, 10.1MB)
# 테스트 19 〉	통과 (0.25ms, 10.2MB)
# 테스트 20 〉	통과 (0.52ms, 10.2MB)