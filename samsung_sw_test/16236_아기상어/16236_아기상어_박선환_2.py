from collections import deque

N = int(input())
space = [list(map(int, input().split())) for _ in range(N)]
D = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1)
]

ci, cj = -1, -1
for i in range(N):
    for j in range(N):
        if space[i][j] == 9:
            ci, cj = i, j
            space[i][j] = 0
            break
    if ci > 0:
        break

baby_size = 2
total_time = 0
cur_eat = 0

while True:
    space_d = [[-1]*N for _ in range(N)]
    queue = deque()
    queue.append((ci, cj, 0))
    p_eat = []
    while queue:
        i, j, d = queue.popleft()
        space_d[i][j] = d
        if not len(p_eat):
            for k in range(4):
                ni = i + D[k][0]
                nj = j + D[k][1]
                if 0 <= ni < N and 0 <= nj < N:
                    if space_d[ni][nj] < 0 and space[ni][nj] <= baby_size:
                        if 0 < space[ni][nj] < baby_size:
                            p_eat.append((ni, nj, d+1))
                        queue.append((ni, nj, d+1))

    min_d = N**2
    p_eat = []
    for i in range(N):
        for j in range(N):
            if 0 < space[i][j] < baby_size:
                if space_d[i][j] == min_d:
                    p_eat.append((i, j))
                elif 0 < space_d[i][j] < min_d:
                    min_d = space_d[i][j]
                    p_eat = [(i, j)]

    if len(p_eat):
        p_eat.sort(key=lambda x: x[1])
        p_eat.sort(key=lambda x: x[0])
        i, j = p_eat[0]
        total_time += min_d
        space[i][j] = 0
        ci, cj = i, j
        cur_eat += 1
        if cur_eat == baby_size:
            baby_size += 1
            cur_eat = 0
    else:
        break

print(total_time)