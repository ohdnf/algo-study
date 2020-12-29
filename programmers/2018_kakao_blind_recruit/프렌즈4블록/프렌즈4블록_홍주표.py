def solution(m, n, board):
    answer = 0
    # 우하향 대각선에 대해 반전시킨 리스트로 변환
    board = [list(line) for line in list(zip(*board))]
    # board가 변하지 않을 때까지
    changed = True
    while changed:
        changed = False
        # 2차원 check 배열을 만들어 각 순회에서 조건에 맞으면 체크
        check = [[False] * m for _ in range(n)]
        # (0, 0) ~ (n-1, m-1) 순회
        for row in range(n-1):
            for col in range(m-1):
                if board[row][col] != '0':
                    if board[row][col] == board[row+1][col] == board[row][col+1] == board[row+1][col+1]:
                        for brow in (row, row+1):
                            for bcol in (col, col+1):
                                check[brow][bcol] = True
        # 순회 종료마다 check 배열의 True 좌표값 찾아 지우기
        for row in range(n):
            for col in range(m):
                if check[row][col]:
                    answer += 1
                    board[row][col] = '0'
                    changed = True

        # 블록 재정렬
        if changed:
            board = [list(''.join(line).replace('0', '').zfill(m)) for line in board]

    return answer


if __name__ == "__main__":
    print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]), 14)
    print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]), 15)


"""
정확성  테스트
테스트 1 〉	통과 (0.06ms, 10.3MB)
테스트 2 〉	통과 (0.07ms, 10.3MB)
테스트 3 〉	통과 (0.02ms, 10.3MB)
테스트 4 〉	통과 (1.28ms, 10.3MB)
테스트 5 〉	통과 (36.06ms, 10.3MB)
테스트 6 〉	통과 (3.93ms, 10.3MB)
테스트 7 〉	통과 (0.71ms, 10.3MB)
테스트 8 〉	통과 (1.22ms, 10.3MB)
테스트 9 〉	통과 (0.05ms, 10.3MB)
테스트 10 〉	통과 (0.66ms, 10.3MB)
테스트 11 〉	통과 (1.51ms, 10.2MB)
"""