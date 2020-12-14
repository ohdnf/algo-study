"""
[목표]
- 상어가 먹을 수 있는 물고기 번호의 합의 최댓값

[상태]
- 4x4 공간
- 각 칸에는 물고기가 있고, 물고기는 번호(1~16)와 방향(상하좌우, 대각선)을 가지고 있다.
- 상어는 (0, 0)에서 시작하고, 방향은 해당 칸에 있는 물고기의 방향을 따른다.

[물고기 이동]
- 상어가 이동한 뒤, 모든 물고기가 번호 순으로 이동한다.
- 물고기는 한 칸만 이동 가능
- 빈 칸/다른 물고기가 있는 칸으로 이동 가능
- 이동할 수 있는 칸이 나올 떄까지 반시계 방향 45도 회전(최대 7번)
- 다른 물고기가 있는 칸으로 이동할 때는 서로 위치 교환 fish1, fish2 = fish2, fish1

[상어 이동]
- 물고기 이동이 끝난 뒤, 현재 방향에 있는 모든 칸 중 물고기가 있는 칸으로 이동
- 상어는 한 번에 여러 칸 이동 가능
- 이동 중에는 물고기 먹지 않음
- 이동한 칸의 물고기를 먹고 해당 물고기의 방향을 갖는다.
- 이동할 수 있는 칸이 없으면 종료
"""
from collections import deque as dq
from copy import deepcopy
import sys
input = lambda: sys.stdin.readline().rstrip()

direction = ((-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1))

area = []
for row in range(4):
    a1, b1, a2, b2, a3, b3, a4, b4 = map(int, input().split())
    area.append([[a1, b1-1], [a2, b2-1], [a3, b3-1], [a4, b4-1]])
del a1, b1, a2, b2, a3, b3, a4, b4

# 상어 배치
max_consumed = area[0][0][0]
area[0][0][0] = 17  # 상어 표시

queue = dq()
queue.append([area, [0, 0, area[0][0][1], max_consumed]])

while queue:
    area, shark = queue.popleft()
    if max_consumed < shark[3]:
        max_consumed = shark[3]
    # 물고기 이동
    for num in range(1, 17):
        # 물고기 위치 파악
        frow, fcol = -1, -1
        for row in range(4):
            for col in range(4):
                if area[row][col][0] == num:
                    frow, fcol = row, col
                    break
            if frow != -1:
                break
        # 물고기 없으면 패스
        if frow == -1:
            continue
        # 물고기 이동 방향 탐색
        fish_num, fish_dir = area[frow][fcol]
        trial = 8
        while trial:
            nrow, ncol = frow + direction[fish_dir][0], fcol + direction[fish_dir][1]
            if 0 <= nrow < 4 and 0 <= ncol < 4 and 0 <= area[nrow][ncol][0] < 17:
                area[frow][fcol], area[nrow][ncol] = area[nrow][ncol], area[frow][fcol]
                break
            # 이동 불가능할 경우 최대 일곱번 반시계방향 45도 회전
            fish_dir = (fish_dir + 1) % 8
            area[frow][fcol][1] = fish_dir  # 이거였다...
            trial -= 1

    # 상어 이동
    srow, scol, sdir, consumed = shark
    area[srow][scol][0] = 0
    # 현재 방향에서 물고기가 있는 칸 탐색
    fish = []
    while True:
        srow, scol = srow + direction[sdir][0], scol + direction[sdir][1]
        if 0 <= srow < 4 and 0 <= scol < 4:
            if area[srow][scol][0]:
                fish.append((srow, scol))
        else:
            break
    # 이동가능한 칸을 BFS
    for row, col in fish:
        temp = deepcopy(area)
        temp[row][col][0] = 17
        queue.append([temp, [row, col, area[row][col][1], consumed + area[row][col][0]]])

print(max_consumed)

"""
메모리 33088 KB
시간 112 ms
"""