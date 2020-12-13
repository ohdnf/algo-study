"""
N*N 격자, N은 홀수
가운데 칸 모래의 양은 0
가운데 칸 좌표는 N//2, N//2
토네이도는 가운데 칸부터 시작, 한 번에 한 칸 이동
x에서 y로 이동하면,
y칸에 있는 모래가 일정한 비율로 정해진 칸들에 흩날림
(예시) 5*5 격자
00 00 02 00 00
00 10 07 01 00
05  a  y<-x 00
00 10 07 01 00
00 00 02 00 00
"""

import sys

input = lambda: sys.stdin.readline()

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

wasd = (
    (   # left
        (-2, 0, 0.02),
        (-1, -1, 0.1), (-1, 0, 0.07), (-1, 1, 0.01),
        (0, -2, 0.05),
        (1, -1, 0.1), (1, 0, 0.07), (1, 1, 0.01),
        (2, 0, 0.02),
    ),
    (  # down
        (-1, -1, 0.01), (-1, 1, 0.01),
        (0, -2, 0.02), (0, -1, 0.07), (0, 1, 0.07), (0, 2, 0.02),
        (1, -1, 0.1), (1, 1, 0.1),
        (2, 0, 0.05),
    ),
    (   # right
        (-2, 0, 0.02),
        (-1, -1, 0.01), (-1, 0, 0.07), (-1, 1, 0.1),
        (0, 2, 0.05),
        (1, -1, 0.01), (1, 0, 0.07), (1, 1, 0.1),
        (2, 0, 0.02),
    ),
    (   # up
        (-2, 0, 0.05),
        (-1, -1, 0.1), (-1, 1, 0.1),
        (0, -2, 0.02), (0, -1, 0.07), (0, 1, 0.07), (0, 2, 0.02),
        (1, -1, 0.01), (1, 1, 0.01),
    ),
)


# 토네이도
def scatter(row, col, index):
    global out
    sand_left = matrix[row][col]
    for drow, dcol, rate in wasd[index]:
        nrow = row + drow
        ncol = col + dcol

        scattered_sand = int(matrix[row][col] * rate)

        if 0 <= nrow < n and 0 <= ncol < n:     # 격자 안
            matrix[nrow][ncol] += scattered_sand
        else:   # 격자 밖
            out += scattered_sand

        sand_left -= scattered_sand

    # a칸 처리
    arow, acol = row + direction[index][0], col + direction[index][1]
    if 0 <= arow < n and 0 <= acol < n:     # 격자 안
        matrix[arow][acol] += sand_left
    else:   # 격자 밖
        out += sand_left
    return


direction = ((0, -1), (1, 0), (0, 1), (-1, 0))  # left down right up
index = 0
limit = 1
move = 0

row = col = n // 2

out = 0

while row >= 0 and col >= 0:
    if matrix[row][col]:
        scatter(row, col, index)
        matrix[row][col] = 0

    if move == limit:
        if index == 1 or index == 3:
            limit += 1

        index += 1
        index %= 4

        move = 0

    row += direction[index][0]
    col += direction[index][1]

    move += 1

print(out)

"""
메모리 39136 KB
시간 1588 ms
"""
