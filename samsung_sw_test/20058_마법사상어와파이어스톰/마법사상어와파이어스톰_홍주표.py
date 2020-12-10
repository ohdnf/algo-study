"""
2^n * 2^n 얼음판 격자에서 파이어스톰 시전
1. 격자를 2^l * 2^l 크기로 나눈다.
2. 모든 `부분격자`를 시계 방향으로 90도 회전
3. 얼음이 있는 칸 3개 또는 그 이상과 인접해있지 않은 칸은 얼음의 양이 1 감소

파이어스톰을 Q번 시전 후 다음 두 가지를 구하시오.
1. 남아있는 얼음의 합
2. 남아있는 얼음 중 가장 큰 덩어리가 차지하는 칸의 개수
덩어리는 얼음이 있는 인접한 칸끼리 연결된 총 개수
"""

from collections import deque as dq
import sys

input = lambda: sys.stdin.readline().rstrip()

n, q = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(2 ** n)]
level = list(map(int, input().split()))

n = 2 ** n
direction = ((-1, 0), (1, 0), (0, -1), (0, 1))


def firestorm(lv):
    if lv:
        lv = 2 ** lv
        temp = [[0] * n for _ in range(n)]
        # 시계 방향 90도 회전
        for row in range(n):
            for col in range(n):
                rq, rr = divmod(row, lv)
                cq, cr = divmod(col, lv)

                temp[lv*rq+cr][lv*cq+lv-1-rr] = area[row][col]
    else:
        temp = area
    # 얼음의 양 감소
    check = [[False] * n for _ in range(n)]
    for row in range(n):
        for col in range(n):
            adj = 0
            for drow, dcol in direction:
                nrow, ncol = row + drow, col + dcol
                if 0 <= nrow < n and 0 <= ncol < n and temp[nrow][ncol]:
                    adj += 1
            if adj < 3:
                check[row][col] = True

    for row in range(n):
        for col in range(n):
            if check[row][col] and temp[row][col]:
                temp[row][col] -= 1

    return temp


# 파이어스톰 시전
for l in level:
    area = firestorm(l)
    # print(f'lv: {l}')
    # for line in area:
    #     print(line)
    # print('-'*30)

total_ice = 0   # 남아있는 얼음의 합
max_size = 0    # 가장 큰 얼음 덩어리가 차지하는 칸의 개수

for row in range(n):
    for col in range(n):
        if area[row][col]:
            size = 1
            total_ice += area[row][col]
            area[row][col] = 0
            queue = dq()
            queue.append((row, col))

            while queue:
                crow, ccol = queue.popleft()
                for drow, dcol in direction:
                    nrow, ncol = crow + drow, ccol + dcol
                    if 0 <= nrow < n and 0 <= ncol < n and area[nrow][ncol]:
                        size += 1
                        total_ice += area[nrow][ncol]
                        area[nrow][ncol] = 0
                        queue.append((nrow, ncol))

            if max_size < size:
                max_size = size

print(total_ice)
print(max_size)
