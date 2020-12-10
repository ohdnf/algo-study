'''
격자크기 2^N x 2^N
A[r][c] 얼음의 양

시전시마다 단계 L 결정
1. 2^L x 2^L 부분격자로 나눈다.
2. 각 부분격자를 시계 방향으로 90도 회전시킨다.
3. 얼음이 있는 칸 3개이상과 인접하지 않은 칸은 -1

출력
1. A[r][c]의 합
2. 얼음 덩어리중 가장 칸을 많이 차지하는 경우의 칸수
입력
1. 첫째줄 N, Q
2. 둘째줄부터 A격자
3. 마지막줄: L들
    2 <= N <=6, 격자크기
    1 <= Q <= Q, 파이어스톰 L의 횟수
    0 <= A[r][c] <= 100
    0 <= L <= N
'''
from pprint import pprint

# 테스트용
# import sys
# sys.stdin = open('input.txt')
T = 6
debug = True

# 제출용
T = 1
debug = False
def dfs(r, c, A):
    # print(r, c)
    # pprint(A)
    A[r][c] = 0
    s = [(r,c)]
    cnt = 1
    # print(f'dfs시작 r,c:{r},{c}, A[r][c]:{A[r][c]}')
    while s:
        r, c = s.pop()
        for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
            nr, nc = r+dr, c+dc
            if 0 <= nr < 2**N and 0 <= nc < 2**N and A[nr][nc]:
                A[nr][nc] = 0
                cnt += 1
                s.append((nr, nc))
    # print(f'return cnt:{cnt}')
    return cnt
    
for case in range(1, T+1):
    N, Q = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(2**N)]
    Ls = list(map(int, input().split()))
    # if case != 4: continue
    # print(f'N:{N}, Q:{Q}, Ls:{Ls}')
    # pprint(A)
    # 1. 파이어스톰 Q회
    # print("sums", sum([ sum(A[i]) for i in range(2**N)] ))
    for L in Ls:
        # 2^l 격자 회전
        temp = [[0] * 2**L for _ in range(2**L)]
        # N:3 => 8
        # L:1
        # N-L:2 => 4
        for dr in range(0, 2**N, 2**L):
            for dc in range(0, 2**N, 2**L):
                for r in range(2**L):
                    for c in range(2**L):
                        # print("size:", 2**L,"입니다", c, (2**L)-1-r, r+dr, c+dc)
                        temp[c][(2**L)-1-r] = A[r+dr][c+dc]
                for r in range(2**L):
                    for c in range(2**L):
                        A[r+dr][c+dc] = temp[r][c]
        # pprint(A)
        
        # 2. 특정 조건에서 얼음 -1
        will_minus = []
        for r in range(2**N):
            for c in range(2**N):
                # (r, c)
                cnt = 0
                for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
                    nr, nc = r+dr, c+dc
                    # 얼음이 -1 되기 위한 조건, 주변에 둘러싼 얼음이 3개 이상이 아니면
                    if not (0 <= nr < 2**N and 0 <= nc < 2**N) or not A[nr][nc]:
                        cnt += 1
                        if cnt == 2:
                            will_minus.append((r, c))
                            break
        # pprint(will_minus)
        for r, c in will_minus:
            if not A[r][c]: continue 
            A[r][c] -= 1
        # pprint(A)
    # pprint(A)
    # 출력-1 : A의 얼음의 양
    sum_of_ice = sum([ sum(A[i]) for i in range(2**N)] )
    # 출력-2 :
    largest = 0
    for r in range(2**N):
        for c in range(2**N):
            # print(r, c, A[r][c])
            if A[r][c]:
                size_of_land = dfs(r, c, A)
                largest = size_of_land if size_of_land > largest else largest
    print(sum_of_ice)
    print(largest)

    # 여기까지 20분

    # 3. 섬찾기