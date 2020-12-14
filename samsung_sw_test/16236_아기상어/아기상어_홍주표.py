"""
n * n 크기 공간에 물고기 m마리와 아기 상어 1마리

아기 상어는 크기 2부터 시작

[아기 상어 이동 방법]
1초에 한 칸 이동
자신의 크기보다 큰 물고기가 있는 칸은 지나갈 수 없다.
자신의 크기보다 작은 물고기만 먹을 수 있다.
크기가 같은 물고기는 먹을 순 없지만 지나갈 수 있다.

더 이상 먹을 수 있는 물고기가 공간에 없다면 엄마 상어에게 도움 요청
먹을 수 있는 물고기 == 1마리 -> 그 물고기 먹으러 가기
먹을 수 있는 물고기 > 1마리 -> 가장 가까운 물고기 먹으러 간다.
거리가 동일하다면 가장 위에 있는 물고기, 가장 왼쪽에 있는 물고기 순으로 먹는다.

물고기를 먹는데 걸리는 시간은 0
자신의 크기와 같은 수의 물고기를 먹으면 크기가 1 증가

[목표]
아기 상어가 엄마 상어에게 도움을 요청하기까지 몇 초가 걸리는지 구하시오
"""
from collections import deque as dq
import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
area = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

# 아기 상어 위치 찾기
srow, scol = -1, -1
for r in range(n):
    for c in range(n):
        if area[r][c] == 9:
            area[r][c] = 0
            srow, scol = r, c
            break
    if srow != -1:
        break

size = 2        # 아기 상어 크기
consumed = 0    # 먹은 물고기 수(진화하면 초기화)
time = 0        # 소요시간
yummies = []    # 먹을 수 있는 물고기 후보군

while True:
    search = dq()
    search.append((srow, scol, 0))
    visited[srow][scol] = True
    min_dist = float('inf')

    # 먹을 수 있는 물고기 찾기
    while search:
        crow, ccol, dist = search.popleft()
        # 후보군 추가
        if 0 < area[crow][ccol] < size:
            yummies.append((crow, ccol, dist))
            if min_dist > dist:
                min_dist = dist
            continue
        # 가지치기
        elif min_dist < dist:
            continue
        # 이동
        for drow, dcol in ((-1, 0), (0, -1), (0, 1), (1, 0)):
            nrow, ncol = crow + drow, ccol + dcol
            if 0 <= nrow < n and 0 <= ncol < n:
                if not visited[nrow][ncol] and 0 <= area[nrow][ncol] <= size:
                    visited[nrow][ncol] = True
                    search.append((nrow, ncol, dist + 1))

    # 먹을 수 있는 물고기 있을 경우
    if yummies:
        # 그 중 가장 가까운 물고기 위치로 가기
        yummies.sort(key=lambda y: (y[2], y[0], y[1]))
        srow, scol, distance = yummies[0]
        area[srow][scol] = 0
        # 냠냠
        consumed += 1
        if consumed == size:
            size += 1
            consumed = 0
        time += distance
        # 후보군 및 방문배열 초기화
        yummies.clear()
        visited = [[False] * n for _ in range(n)]
    # 먹을 수 있는 물고기 없을 경우
    else:
        break

print(time)

"""
메모리 33032 KB
시간 100 ms

20 * 20 테스트
20
9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3
3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3
3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3
3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3
3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3
4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4
4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4
4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4
5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6

399
"""
