def solution(msg):
    answer = []
    lzw = {
        'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5,
        'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10,
        'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15,
        'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20,
        'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25,
        'Z': 26
    }
    head = 0
    while head < len(msg):
        tail = head + 1

        while msg[head:tail] in lzw and tail <= len(msg):
            tail += 1

        next_index = len(lzw) + 1
        if msg[head:tail] not in lzw:
            lzw[msg[head:tail]] = next_index
        
        if tail - 1 == head:
            answer.append(lzw[msg[head:tail]])
            head = tail
        else:
            answer.append(lzw[msg[head:tail-1]])
            head = tail - 1

    return answer

"""
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.03ms, 10.2MB)
테스트 3 〉	통과 (0.02ms, 10.3MB)
테스트 4 〉	통과 (0.40ms, 10.3MB)
테스트 5 〉	통과 (0.04ms, 10.2MB)
테스트 6 〉	통과 (0.56ms, 10.3MB)
테스트 7 〉	통과 (0.44ms, 10.2MB)
테스트 8 〉	통과 (0.51ms, 10.3MB)
테스트 9 〉	통과 (0.01ms, 10.2MB)
테스트 10 〉	통과 (0.52ms, 10.2MB)
테스트 11 〉	통과 (0.44ms, 10.2MB)
테스트 12 〉	통과 (0.59ms, 10.3MB)
테스트 13 〉	통과 (1.24ms, 10.2MB)
테스트 14 〉	통과 (0.90ms, 10.3MB)
테스트 15 〉	통과 (0.89ms, 10.3MB)
테스트 16 〉	통과 (0.70ms, 10.3MB)
테스트 17 〉	통과 (0.53ms, 10.3MB)
테스트 18 〉	통과 (0.19ms, 10.1MB)
테스트 19 〉	통과 (0.24ms, 10.3MB)
테스트 20 〉	통과 (0.51ms, 10.2MB)
"""
