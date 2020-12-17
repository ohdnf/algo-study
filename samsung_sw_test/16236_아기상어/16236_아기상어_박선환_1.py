from collections import deque

N = int(input())
space = [list(map(int, input().split())) for _ in range(N)]
D = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1)
]

p_move = deque()
for i in range(N):
    for j in range(N):
        if space[i][j] == 9:
            p_move.append((i, j))
            space[i][j] = 0
            break

baby_size = 2
total_time = 0
cur_time = 0
cur_eat = 0

while True:
    visited = [[0]*N for _ in range(N)]
    # for i, j in p_move:
    #     visited[i][j] = 1
    p_eat = []
    tmp_p_move = deque()
    while len(p_move):
        i, j = p_move.popleft()
        for k in range(4):
            ni = i + D[k][0]
            nj = j + D[k][1]
            if 0 <= ni < N and 0 <= nj < N:
                if not visited[ni][nj] and space[ni][nj] <= baby_size:
                    visited[ni][nj] = 1
                    tmp_p_move.append((ni, nj))
                    if 0 < space[ni][nj] < baby_size:
                        p_eat.append((ni, nj))
    p_move = tmp_p_move
    if len(p_eat):
        cur_time += 1
        p_eat.sort(key=lambda x: x[1])
        p_eat.sort(key=lambda x: x[0])
        i, j = p_eat[0]
        space[i][j] = 0
        cur_eat += 1
        if cur_eat == baby_size:
            baby_size += 1
            cur_eat = 0
        p_move = deque()
        p_move.append((i, j))
        total_time += cur_time
        cur_time = 0
    else:
        cur_time += 1

    go = False
    for i in range(N):
        for j in range(N):
            if 0 < space[i][j] < baby_size:
                go = True
                break
        if go:
            break
    if not go:
        break

print(total_time)