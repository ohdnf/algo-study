# 12:47 - 2:15 테케 통과
'''
입력
1. N, M, K: 격자크기, 상어 개체수, 채취 지속시간
2. M마리의 상어의 우선순위
    위1, 아래2, 왼쪽3, 오른쪽4
상어의 이동 규칙
1. 아무 냄새 없는 칸 > 내 칸
    & 동일 우선순위 내에서 방향 우선순위가 존재한다.
2. 방금 이동한 방향이 바라보는 방향이 된다.
3. 한칸에 여러상어가 모이면. 1명만 남고 쫓겨난다.
'''
from pprint import pprint
import sys

# 테스트용
sys.stdin = open('input.txt')
T = 4
debug = False

# 제출용
# input = sys.stdin.readline
# T = 1
# debug = False

direction = {
    1: (-1, 0),
    2: ( 1, 0),
    3: ( 0,-1),
    4: ( 0, 1)
}
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    field = [list(map(int, input().split())) for _ in range(N)] # 상어아닌 채취
    record = [[0]*N for _ in range(N)] # xtime때 뿌려진 채취란 기록
    initial_head = [0] + list(map(int, input().split())) # [0]은 인덱스 맞춰주기용
    if debug:
        print(f'initial_head:{initial_head}')
        pprint(f'record{record}')
        pprint(f'field{field}')
    # 0-1. 초기 상어 위치
    sharks = dict()
    for r in range(N):
        for c in range(N):
            if field[r][c]:
                record[r][c] = 0
                number = field[r][c]
                sharks[(r,c)] = (number, initial_head[number])
    if debug:
        print(f'sharks:{sharks}')
    
    priority = [[]] # []는 인덱스 맞추기용
    for i in range(1, M+1): # 상어 M마리
        temp = [()] # 인덱스 맞추기용
        for _ in range(4): # 위1, 아래2, 왼3, 오른3 각 방향 우선순위
            temp.append(tuple(map(int, input().split())))
        priority.append(temp)
    if debug:
        pprint(f'priority{priority}')
    
    time = 0 # 1000초 초과하면 -1리턴
    remain = M # 남은 상어수
    
    while time <= 999:
        # 1. 각 상어가 움직인다.
        next_sharks = dict()
        for pos, values in sharks.items():
            r, c = pos
            number, head = values
            # 이전칸 상어 흔적 삭제
            # field[r][c] = 0
            # a. 아무 냄새 없는 칸
            # print(f'우선순위, head:{head}, priority:{priority[number][head]}')
            for d in priority[number][head]: # 해당 방향 우선순위 대로 꺼냄
                dr, dc = direction[d]
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < N and (not field[nr][nc] or time - record[nr][nc] >= K):
                    if (nr, nc) not in next_sharks:
                        next_sharks[(nr,nc)] = (number, d)
                    else:
                        # 2. 같은 칸의 상어는 대결한다, 번호 낮은 놈이 이긴다.
                        if next_sharks[(nr,nc)][0] > number:
                            next_sharks[(nr,nc)] = (number, d) # 이겼다.
                            # 지면 국물도 없다.
                        remain -= 1 # 상어 한 마리가 죽었다.
                    break
            # b. 아무 냄새 없는 칸이 없다 => 내 채취 칸
            else:
                for d in priority[number][head]:
                    dr, dc = direction[d]
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < N and 0 <= nc < N and field[nr][nc] == number:
                        if (nr, nc) not in next_sharks:
                            next_sharks[(nr,nc)] = (number, d)
                        else:
                            # 2. 같은 칸의 상어는 대결한다, 번호 낮은 놈이 이긴다.
                            if next_sharks[(nr,nc)][0] > number:
                                next_sharks[(nr,nc)] = (number, d) # 이겼다.
                                # 지면 국물도 없다.
                            remain -= 1 # 상어 한 마리가 죽었다.
                        break
        sharks = next_sharks
        time += 1
        if debug:
            print(f'time:{time},next_sharks:{next_sharks}')
        if remain == 1: # 1번 남어만 남았다.
            break
        s = [[0]*N for _ in range(N)]
        for pos, values in next_sharks.items():
            r, c = pos
            number, head = values
            s[r][c] = number
            field[r][c] = number
            record[r][c] = time
        if debug:
            print(time)
            pprint(s)
            pprint(field)
            pprint(record)
    # 출력
    if remain != 1:
        print(-1)
    else:
        print(time)