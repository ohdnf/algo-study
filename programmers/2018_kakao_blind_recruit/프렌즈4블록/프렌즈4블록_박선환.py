def solution(m, n, board):
    answer = 0
    for i in range(len(board)):
        board[i] = list(board[i])
    
    while True:
        # 삭제할 블록 찾아내기
        b_to_remove = []
        for i in range(m-1):
            for j in range(n-1):
                start = board[i][j]
                if start == '-':
                    continue
                if start == board[i][j+1] and start == board[i+1][j] and start == board[i+1][j+1]:
                    b_to_remove.append([i, j])
        if not b_to_remove: # 삭제할 블록 없을 경우 멈추기
            break
                
        # 블록 삭제
        for i, j in b_to_remove:
            for k in range(2):
                for l in range(2):
                    if board[i+k][j+l] != '-':
                        answer += 1
                        board[i+k][j+l] = '-'

        # 블록 아래로 밀어내기
        for i in range(m):
            for j in range(n):
                if board[i][j] == '-':
                    k = 0
                    while 0 < i-k:                        
                        board[i-k][j] = board[i-1-k][j]
                        board[i-1-k][j] = '-'
                        k += 1
    
    return answer

'''
정확성 테스트
테스트 1 〉	통과 (0.05ms, 10.3MB)
테스트 2 〉	통과 (0.08ms, 10.3MB)
테스트 3 〉	통과 (0.01ms, 10.4MB)
테스트 4 〉	통과 (4.11ms, 10.3MB)
테스트 5 〉	통과 (309.97ms, 10.4MB)
테스트 6 〉	통과 (18.72ms, 10.3MB)
테스트 7 〉	통과 (2.24ms, 10.2MB)
테스트 8 〉	통과 (6.41ms, 10.2MB)
테스트 9 〉	통과 (0.04ms, 10.3MB)
테스트 10 〉	통과 (1.54ms, 10.3MB)
테스트 11 〉	통과 (9.62ms, 10.3MB)
'''