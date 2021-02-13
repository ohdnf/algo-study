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