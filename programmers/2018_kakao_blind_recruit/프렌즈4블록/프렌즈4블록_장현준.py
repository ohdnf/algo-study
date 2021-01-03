def solution(m, n, board):
    board = [list(row) for row in board]
    answer = 0

    while True:
        # 1. 제거 리스트 생성 => 범위 0 ~ N-2
        removes = [] # 2x2의 10시방향 좌표만 등록
        for r in range(m-1):
            for c in range(n-1):
                if not board[r][c]: # 제거된 블록 건너띔
                    continue
                for dr, dc in [(1,0), (0,1),(1,1)]:
                    nr, nc = r+dr, c+dc
                    if board[r][c] != board[nr][nc]: # 조건 미충족
                        break
                else:
                    # 2x2 생성
                    removes.append((r,c))
        # 종료조건
        if not removes:
            return answer
        # 2. 제거
        for r, c in removes:
            for dr, dc in [(0,0), (1,0), (0,1), (1,1)]:
                nr, nc = r+dr, c+dc
                if board[nr][nc]:
                    board[nr][nc] = 0
                    answer += 1
        
        # 3. 공백 채우기
        for c in range(n):
            for r in range(m-1, 0, -1): # r == 0 칸은 탐색 제외
                # 공백칸 발견
                if not board[r][c]:
                    idx = r # 첫번째 공백칸
                    for r in range(r-1, -1, -1):
                        if board[r][c]:
                            board[idx][c], board[r][c] = board[r][c], 0
                            idx -= 1
                    else:
                        # 공백 채우기 끝
                        break
'''
테스트 1 〉	통과 (0.04ms, 10.3MB)
테스트 2 〉	통과 (0.06ms, 10.3MB)
테스트 3 〉	통과 (0.01ms, 10.3MB)
테스트 4 〉	통과 (1.71ms, 10.3MB)
테스트 5 〉	통과 (36.54ms, 10.3MB)
테스트 6 〉	통과 (3.91ms, 10.3MB)
테스트 7 〉	통과 (0.86ms, 10.2MB)
테스트 8 〉	통과 (1.37ms, 10.4MB)
테스트 9 〉	통과 (0.05ms, 10.4MB)
테스트 10 〉통과 (0.63ms, 10.3MB)
테스트 11 〉통과 (1.58ms, 10.2MB)
'''