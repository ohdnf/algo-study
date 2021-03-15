def solution(board, moves):
    answer = 0
    stack = []
    LENGTH = len(board)
    for move in moves:
        move -= 1
        depth = 0
        while depth < LENGTH:
            if board[depth][move]:
                if stack and stack[-1] == board[depth][move]:
                    stack.pop()
                    answer += 2
                else:
                    stack.append(board[depth][move])
                board[depth][move] = 0
                break
            depth += 1
        
    return answer

"""
테스트 1 〉	통과 (0.02ms, 10.2MB)
테스트 2 〉	통과 (0.02ms, 10.2MB)
테스트 3 〉	통과 (0.02ms, 10.3MB)
테스트 4 〉	통과 (4.25ms, 10.1MB)
테스트 5 〉	통과 (0.02ms, 10.2MB)
테스트 6 〉	통과 (0.02ms, 10.1MB)
테스트 7 〉	통과 (0.08ms, 10.2MB)
테스트 8 〉	통과 (0.41ms, 10.1MB)
테스트 9 〉	통과 (0.37ms, 10.2MB)
테스트 10 〉	통과 (0.45ms, 10.2MB)
테스트 11 〉	통과 (1.12ms, 10.2MB)
"""
