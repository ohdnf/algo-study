'''
NxN 격자, A[r][c] 모래의 양
토네이도
    - 격자 가운데 칸부터 시작
    - 한 번에 한칸 이동
    - 일정한 비율로 흩날림 (소수점 아래 날림 => 정수)
    - 나머지 알파에 남음
    - 1,1까지 이동후 소멸, 격자 밖으로 나간 모래의 양
입력
    첫째줄: N
    둘째줄부터 N줄: A
    3 <= N <= 499, N 홀수
    0 <= A[r][c] <= 1000
    가운데 칸 모래의 양 0
'''

import sys
from pprint import pprint

#테스트용
sys.stdin = open('input.txt')
debug = True
T = 6

# 제출용
# input = sys.stdin.readline
# debug = False
# T = 1
for case in range(1, T+1):
        
    # 입력
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    # pprint(A)

    # 코드 플랜
    # 1. 가운데 부터 시작한다.
    res = 0 # 버려지는 모래의 양
    direction = {
        0: ( 0,-1), # 서
        1: ( 1, 0), # 남
        2: ( 0, 1), # 동
        3: (-1, 0), # 북
    }
    # 토네이도 direction
    td = (
        # (가던 방향, 수직방향( (방향+1)%4, (방향+3)%4 )
        # (1, 0), # y
        (0, 1, 1), # 1% 양쪽
        (1, 1, 7), # 7% 양쪽
        (1, 2, 2), # 2% 양쪽
        (2, 1, 10), # 10% 양쪽
        # (2, 0), # 알파
        (3, 0, 5), # 5% 1개
    )
    # a. 토네이도 이동 방향은 서남동북순으로 반복한다.
    
    x = (N//2, N//2)
    r, c = (N//2, N//2) # 가운데 지점
    d = 0 # 처음 이동할 토네이도 서남동북 방향

    while True:
        for _ in range(1 + d//2):
            if debug: pprint(A);
            dr, dc = direction[d%4] # 토네이도 방향
            dr1, dc1 = direction[(d+1)%4] # 수직방향1 
            dr2, dc2 = direction[(d+3)%4] # 수직방향2
            y = (x[0]+dr, x[1]+dc)
            sand = A[y[0]][y[1]]
            A[y[0]][y[1]] = 0
            remain = sand # 알파 관련
            if debug: print(f'y:{y}, sand:{sand}');
            for a, b, percent in td:
                if b == 0:
                    r = x[0] + (dr * a)
                    c = x[1] + (dc * a)
                    calc = int( sand * (percent * 0.01) )
                    if 0 <= r < N and 0 <= c < N:
                        A[r][c] += calc
                    else:
                        res += calc # 격자 밖으로 버려짐
                    remain -= calc
                else:
                    for xr, xc in ((dr1, dc1), (dr2, dc2)):
                        r = x[0] + (dr * a) + (xr * b)
                        c = x[1] + (dc * a) + (xc * b)
                        calc = int( sand * (percent * 0.01) )
                        if 0 <= r < N and 0 <= c < N:
                            A[r][c] += calc
                        else:
                            res += calc # 격자 밖으로 버려짐
                        remain -= calc
            # 알파
            r = y[0] + (dr * 1)
            c = y[1] + (dc * 1)
            if 0 <= r < N and 0 <= c < N:
                A[r][c] += remain
            else:
                res += remain # 격자 밖으로 버려짐
            
            if y == (0, 0):
                break
            x = y
        else:
            d += 1
            continue
        break
    if debug: pprint(A);
    print(res)
    '''
    메모리: 126.536MB, 276ms
    '''