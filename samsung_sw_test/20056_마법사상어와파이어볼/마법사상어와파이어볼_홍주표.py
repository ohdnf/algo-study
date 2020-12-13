"""
n*n 격자에 파이어볼 m개 발사

격자의 1번 행은 N번 행과 연결, 1번 열은 N번 열과 연결되어 있다.

파이어볼 이동이 끝난 후 2개 이상의 파이어볼이 한 격자 칸에 모여있으면,
1. 파이어볼들을 모두 합친다.
2. 4개로 나눈다.
3. 나눠진 파이어볼의 특성은 다음과 같다.
3-1. 질량 = (파이어볼들의 질량 총합) // 5
3-2. 속력 = (파이어볼들의 속력 총합) // (파이어볼의 개수)
3-3. 파이어볼들의 방향이 모두 홀수이거나 짝수이면 (0, 2, 4, 6), 그렇지 않으면 (1, 3, 5, 7)로 쪼개진다.
4. 질량이 0인 파이어볼은 소멸

이동 명령 K번 후 남아있는 파이어볼의 질량의 합을 구하라
"""

import sys
input = lambda: sys.stdin.readline()

n, m, k = map(int, input().split())
fireballs = [list(map(int, input().split())) for _ in range(m)]  # r, c, m, s, d

direction = {
    0: (-1, 0),
    1: (-1, 1),
    2: (0, 1),
    3: (1, 1),
    4: (1, 0),
    5: (1, -1),
    6: (0, -1),
    7: (-1, -1)
}


def get_new_coord(r, c, s, d):
    dr, dc = direction[d]
    # nr = (r + dr * (s % n)) % n
    # nc = (c + dc * (s % n)) % n
    nr = (r + dr * s) % n
    nc = (c + dc * s) % n
    return nr, nc


while k > 0:
    k -= 1

    # 파이어볼 이동
    overlapped = set()  # 겹치는 파이어볼 좌표
    coord = dict()  # 좌표별 파이어볼 배열
    while fireballs:
        r, c, m, s, d = fireballs.pop()
        r, c = get_new_coord(r, c, s, d)

        if r in coord:
            if c in coord[r]:  # 해당 칸에 파이어볼 존재
                overlapped.add((r, c))
                coord[r][c].append((m, s, d))
            else:
                coord[r][c] = [(m, s, d)]
        else:
            coord[r] = dict()
            coord[r][c] = [(m, s, d)]

    # print(overlapped)
    # print(coord)

    # 겹치는 파이어볼 처리
    while overlapped:
        r, c = overlapped.pop()
        new_m = new_s = even = odd = total = 0
        for m, s, d in coord[r][c]:
            total += 1
            new_m += m
            new_s += s
            if d % 2:
                odd += 1
            else:
                even += 1

        coord[r][c].clear()

        new_m //= 5
        new_s //= total

        if new_m:
            if even and odd:
                for new_d in (1, 3, 5, 7):
                    new_r, new_c = get_new_coord(r, c, new_s, new_d)
                    coord[r][c].append([new_m, new_s, new_d])
            else:
                for new_d in (0, 2, 4, 6):
                    new_r, new_c = get_new_coord(r, c, new_s, new_d)
                    coord[r][c].append([new_m, new_s, new_d])

    # 다음 명령에 이동할 파이어볼 저장
    for r in coord:
        for c in coord[r]:
            for m, s, d in coord[r][c]:
                fireballs.append([r, c, m, s, d])

# print(coord)

answer = 0
for r in coord:
    for c in coord[r]:
        for m, _, _ in coord[r][c]:
            answer += m

print(answer)


"""
메모리 31388 KB
시간 812 ms
코드 길이 2231 B
"""