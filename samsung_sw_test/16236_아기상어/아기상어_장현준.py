'''
NxN 격자
물고기 M마리 & 1마리 상어 (초기값2)
한 칸에 물고기 최대 1 마리

이동규칙
아기 상어
    1. 자신보다 나이 많은 물고기칸으로 이동불가
    2. 자신보다 나이 적은 물고기 섭취 가능
    3. 동갑 물고기칸으로 이동만 가능
룰
    1. 먹을수 없는 물고기가 없다면 엄마를 부른다.
    2. 먹을 수 있는 물고기중 가장 가깝고 r이 작고, c가 작은 물고기를 먹는다.
    3. 자신의 나이만큼 먹을때마다 나이가 1 증가한다.
엄마를 부르기까지 걸리는 시간은?
입력
N : 격자크기 2<=N<=20
N줄 : 필드
    0: 빈칸
    1,2,3,4,5,6: 물고기
    9: 아기 상어 위치
'''
from pprint import pprint
import sys
sys.stdin = open('input.txt') 
from collections import deque
T = 6
debug = False

for tc in range(1, T+1):
    N = int(input())
    field = [list(map(int, input().split())) for _ in range (N)]
    if tc != 4: continue
    visited = [[-1]*N for _ in range(N)] # time
    for r in range(N):
        for c in range(N):
            if field[r][c] == 9: #상어
                field[r][c] = 0
                visited[r][c] = 0
                q = deque([(r, c)])
                break
        else:
            continue
        break
    if debug:
        pprint(field)
        pprint(visited)
        
    # 다음 희생양을 찾는다 => 실패시 종료
    # 먹는다
    age = 2
    eaten = 0
    time = -1
    last_eat = 0
    if debug:
        print(age)
    while q:
        time += 1
        candidate = []
        if debug:
            print(f'지금이순간:{time}')
        for _ in range(len(q)):    
            r, c = q.popleft()
            for dr, dc in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= N or nc < 0 or nc >= N: # 격자 범위 초과
                    continue
                # 물고기 발견
                if candidate:
                    # 1. 나이 적은 물고기 => 후보 등록
                    if 0 < field[nr][nc] < age:
                        candidate.append([(nr, nc)])
                else:
                    # 1. 나이 적은 물고기 => 후보 등록
                    if 0 < field[nr][nc] < age:
                        candidate.append([(nr, nc)])
                        visited[nr][nc] = time + 1
                    # 2. 동갑 물고기 => 지나간다.
                    elif field[nr][nc] == age:
                        q.append((nr, nc))
                        visited[nr][nc] = time + 1
                    # 3. 나이 많은 물고기 => 암것도 못한다.
                    elif field[nr][nc] > age:
                        continue
                    # 4. 물고기 없는칸 & 이번에 들른적 없다.   0  2  1  2  0
                    if visited[nr][nc] <= last_eat:
                        q.append((nr,nc))
                        visited[nr][nc] = time + 1
        if not candidate: continue
        r1, c1 = candidate[0]
        for r2, c2 in candidate[1:]:
            if r2 < r1 or (r2 == r1 and c2 < c1):
                r1, c1 = r2, c2
        q = deque([(r1, c1)])
        field[r1][c1] = 0
        eaten += 1
        last_eat = time + 1
        visited[nr][nc] = time + 1
        if eaten == age:
            eaten = 0
            age += 1
        if debug:
            pprint(field)
            pprint(visited)
    print(last_eat)