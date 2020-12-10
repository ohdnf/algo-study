import math

D = [
    (-1, 0),
    (-1, 1),
    (0, 1),
    (1, 1),
    (1, 0),
    (1, -1),
    (0, -1),
    (-1, -1)
]

N, M, K = map(int, input().split())
fireballs = [list(map(int, input().split())) for _ in range(M)]

for _ in range(K):
    matrix = list([0] * N for _ in range(N))
    for ball in fireballs:
        r, c, m, s, d = ball
        nr = (r + D[d][0]*s) % N
        nc = (c + D[d][1]*s) % N
        if matrix[nr][nc] == 0:
            matrix[nr][nc] = [(m, s, d)]
        else:
            matrix[nr][nc].append((m, s, d))
    
    fireballs = []
    for i in range(N):
        for j in range(N):
            if matrix[i][j] != 0:
                balls = matrix[i][j]
                if len(balls) >= 2:
                    nm = 0
                    ns = 0
                    nd = balls[0][2] % 2
                    is_same = True
                    for ball in balls:
                        nm += ball[0]
                        ns += ball[1]
                        if ball[2] % 2 != nd:
                            is_same = False
                    nm = math.floor(nm / 5)
                    ns = math.floor(ns / len(balls))
                    if nm:
                        if is_same:
                            for d in [0, 2, 4, 6]:
                                fireballs.append([i, j, nm, ns, d])
                        else:
                            for d in [1, 3, 5, 7]:
                                fireballs.append([i, j, nm, ns, d])
                else:
                    fireballs.append([i, j, balls[0][0], balls[0][1], balls[0][2]])
answer = 0
for ball in fireballs:
    answer += ball[2]

print(answer)

# 메모리: 33236KB
# 시간: 872ms