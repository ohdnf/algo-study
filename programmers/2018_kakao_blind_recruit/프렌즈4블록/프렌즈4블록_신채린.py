def solution(m, n, board):
    board = [list(board[i]) for i in range(m)]
    answer = 0
    def func():
        count = 0
        used = [[0]*n for _ in range(m)]
        erase = []
        # 차례대로 돌면서, 오른쪽, 아래, 대각선 방향이 (2x2 블록이) 같은 블록이라면 지운다. 
        for i in range(m):
            for j in range(n):
                if 0 <= i+1 < m and 0<= j+1 < n:
                    if board[i][j] == board[i][j+1] == board[i+1][j] == board[i+1][j+1] and board[i][j]!=0:
                        # 4개의 블록들을 모두 -1로 표시를 해둔다.
                        used[i][j], used[i][j+1], used[i+1][j], used[i+1][j+1] = -1, -1, -1, -1
                        count += 1
        # 만약 지워질 블록들이 없다면 False
        if count == 0:
            return False
        # 지워질 블록들이 있다면 used 배열을 리턴한다. 
        else:
            return used
    
    # 지워질 블록들이 없을 때까지 반복한다.
    while True:
        res = func() 
        if res == False:
            break
        else:
            # 지워질 블록들이 몇 개인지 카운팅하기 + 0으로 바꾸기
            for i in range(m):
                for j in range(n):
                    if res[i][j] == -1:
                        board[i][j] = 0
                        answer += 1

            # 위에서 아래로 떨어뜨려서 빈 공간 채우기 
            for i in range(m):
                for j in range(n):
                    if board[i][j] == 0:
                        k = 0
                        while 0 < i-k:                        
                            board[i-k][j] = board[i-1-k][j]
                            board[i-1-k][j] = 0
                            k += 1

    return answer