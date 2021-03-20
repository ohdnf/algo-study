def solution(board, moves):
    stack = []
    answer = 0
    for move in moves:
        for i in range(len(board)):
            if board[i][move-1] != 0:
                current = board[i][move-1]
                board[i][move-1] = 0
                 # stack 에서 같은 모양의 인형인지 확인하기. 
                if stack and current == stack[-1]:
                    stack.pop() 
                    answer += 2
                else:
                    stack.append(current)
                break
            else:
                continue 
           
    return answer