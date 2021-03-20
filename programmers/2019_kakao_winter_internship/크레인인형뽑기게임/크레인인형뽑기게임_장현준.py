def solution(board, moves):
    def push_stack(stack, n):
        if len(stack) == 0 or stack[-1] != n:
            stack.append(n)
            return 0
        stack.pop()
        return 2
    stack = []
    answer = 0
    for col in moves:
        col -= 1
        for row in range(len(board)):
            if board[row][col]:
                answer += push_stack(stack, board[row][col])
                board[row][col] = 0
                break
    return answer
'''
정확성  테스트
테스트 1 〉	통과 (0.02ms, 10.3MB)
테스트 2 〉	통과 (0.04ms, 10.2MB)
테스트 3 〉	통과 (0.03ms, 10.1MB)
테스트 4 〉	통과 (1.87ms, 10.2MB)
테스트 5 〉	통과 (0.03ms, 10.1MB)
테스트 6 〉	통과 (0.03ms, 10.2MB)
테스트 7 〉	통과 (0.12ms, 10.2MB)
테스트 8 〉	통과 (0.45ms, 10.1MB)
테스트 9 〉	통과 (0.40ms, 10.1MB)
테스트 10 〉통과 (0.50ms, 10.2MB)
테스트 11 〉통과 (1.11ms, 10.4MB)
'''