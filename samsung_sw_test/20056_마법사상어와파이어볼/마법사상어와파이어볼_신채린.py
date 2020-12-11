N, M, K = map(int, input().split())
directions = {
    0: (-1, 0), 
    1: (-1, 1), 
    2: (0, 1), 
    3: (1, 1), 
    4: (1, 0), 
    5: (1, -1), 
    6: (0, -1), 
    7: (-1, -1)
}
fireballs = [list(map(int, input().split())) for _ in range(M)]
for _ in range(K):
    info = dict()
    coordinates = set()
    for fireball in fireballs:
        r, c, m, s, d = fireball
        # 방향대로 이동하기 
        # 방향 구하기
        r = (r + directions[d][0]*s) % N
        c = (c + directions[d][1]*s) % N

        # hash로 처리하기 
        hashed= str(r) + "/" + str(c)
        if hashed in info:
            info[hashed].append([m, s, d])
        else:
            info[hashed] = [[m, s, d]]
            coordinates.add((r, c))

    # 파이어볼 합치기
    fireballs =[]
    for coord in coordinates:
        r, c = coord
        hashed = str(r) + "/" + str(c)
        # 만약 겹치는 좌표가 없다면 
        if len(info[hashed]) == 1:
            m, s, d = info[hashed][0]
            fireballs.append([r, c, m, s, d])
        # 만약 겹치는 좌표가 있다면 
        else:
            tot_mass = 0
            tot_velocity = 0
            direction = 99999
            direction_changed = False
            odd = 0
            even = 0
            # 해당 좌표의 각 파이어볼마다 
            for each in info[hashed]:
                m, s, d = each
                tot_mass += m
                tot_velocity += s
                # 방향이 바뀌는지 안바뀌는지 확인한다.
                if d % 2 == 0:
                    even += 1
                else:
                    odd += 1

            # 질량 구하기
            m = int(tot_mass/5)
            s = int(tot_velocity/len(info[hashed]))
            #방향이 바뀌었다면 
            if even and odd:
                d = [1, 3, 5, 7]
            # 방향이 바뀌지 않았다면 
            else:
                d = [0, 2, 4, 6]
            # 만약 질량이 0 이 아니면 fireballs 배열에 추가한다.
            if m != 0:
                for i in range(4):
                    fireballs.append([r, c, m, s, d[i]])
#총 질량 구하기
ans = 0
for coord in fireballs:
    ans += coord[2]
print(ans)

# 기존 방식은 왜 안됐을까?
        # 방향대로 이동하기 
        # 방향 구하기
        r = (r + directions[d][0]*s)
        c = (c + directions[d][1]*s)
        # N 보다 크거나, 1보다 작을 때 처리하기 
        if r > N:
            r %= N
        elif r < 1:
            r = N - (abs(r) % N)
        if c > N:
            c %= N
        elif c < 1:
            c = N - (abs(c) % N)

#메모리: 31632KB	
#시간: 980ms