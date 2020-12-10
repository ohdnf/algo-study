'''
N: NxN격자크기, M: 파이어볼 갯수, K: 명령 횟수
위치:r,c 질량:m 속력:s 방향:d
명령
    1. 모든 파이어볼이 방향과 속력만큼 이동한다. (이동후 같은 칸에 파이어볼 중복 가능)
    2. 이동이 모든 끝난후, 같은칸의 파이어볼은 1개로 합쳐진다.
    3. 파이어볼은 4개로 나뉜다.
        a. 질량: 질량합/5
        b. 속력: 속력합/합쳐진갯수
        c. 방향: 모두 홀수 or 짝수이면 0,2,4,6 or 1,3,5,7
        d. 질량0인 파이어볼은 소멸
'''
from pprint import pprint
import collections

def testing(d):
    direction2 = {
        0:"↑",
        1: "↗",
        2: "→",
        3: "↘",
        4: "↓",
        5: "↙",
        6: "←",
        7: "↖",
        }
    field = [ list(["0,00"] for _ in range(N)) for _ in range(N)]
    for k, v in d.items():
        r, c = k
        field[r-1][c-1] = [str(m)+","+str(s)+direction2[d] for m, s, d in v]
    if debug:
        pprint(field)
# 제출용
# T = 1
# debug = False

#테스트용
import sys
sys.stdin = open('input.txt')
T = 4
debug = False

for case in range(1, T+1):
    
    N, M, K = map(int, input().split())
    direction = {
        0: (N-1, 0),
        1: (N-1, 1),
        2: (0, 1),
        3: (1, 1),
        4: (1, 0),
        5: (1, N-1),
        6: (0, N-1),
        7: (N-1, N-1)
    }
    fireballs = collections.defaultdict(list)
    for _ in range(M):
        r, c, m, s, d = map(int, input().split())
        fireballs[(r,c)].append((m, s, d))
    # if case != 4: continue
    if debug:
        print(fireballs)
        testing(fireballs)

    for k in range(1, K+1):
        # print(k, "fireballs")
        # temp_fireballs: fireballs가 이동한것을 일시 저장!
        temp_fireballs = collections.defaultdict(list)

        # 이동 시작 d방향으로 s칸 만큼 이동
        for pos, fbs in fireballs.items():
            r, c = pos
            for fb in fbs: #파이어볼을 하나씩 꺼낸다.
                m, s, d = fb
                dr, dc = direction[d]
                nr, nc = (r+(dr*s)) % N, (c+(dc*s)) % N
                if debug:
                    print(nr, nc)
                temp_fireballs[(nr, nc)].append((m, s, d))
        if debug:
            print(k, "temp")
            testing(temp_fireballs)

        # next_fireballs: temp_fireballs가 합치고, 나눠지는 작업 저장!
        next_fireballs = collections.defaultdict(list)
        for pos, fbs in temp_fireballs.items():
            r, c = pos
            if debug:
                print("pos, fbs", pos, fbs)
            if len(fbs) == 1:
                next_fireballs[pos] = fbs
                continue;
            cnt = sum_m = sum_s = isEven = isOdd = 0
            for fb in fbs:
                cnt += 1
                m, s, d = fb
                sum_m += m
                sum_s += s
                if d % 2:
                    isOdd = 1
                else:
                    isEven = 1
            sum_m //= 5 # 질량은 ⌊(합쳐진 파이어볼 질량의 합)/5⌋이다.
            sum_s //= cnt # 속력은 ⌊(합쳐진 파이어볼 속력의 합)/(합쳐진 파이어볼의 개수)⌋
            if debug:
                print(f'r:{r}, c:{c}, sum_m:{sum_m}, sum_s:{sum_s}')

            if not sum_m: # m이 0이면 파이어볼 삭제
                continue

            ds = (1, 3, 5, 7) if isEven and isOdd else (0, 2, 4, 6)
            for d in ds:
                next_fireballs[pos].append((sum_m, sum_s, d))
            if debug:
                print(f'next_fireballs[{pos}].append(({sum_m}, {sum_s}, {ds}))')
        fireballs = next_fireballs
        if debug:
            print(k, "next")
            testing(next_fireballs)
    res = 0
    for pos, fbs in fireballs.items():
        for fb in fbs: # m, s, d
            if debug:
                print(fb[0])
            res += fb[0] # m을 더한다.
    print(res)
    # 출력: K번 명령후, 남아있는 파이어볼 질량의 합 출력

'''
메모리 149.456MB, 420ms
'''