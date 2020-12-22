# 10:53

'''
4x4 격자, (x,y)
각 칸에는 물고기 1마리(번호, 방향)
    1 <= 번호 <=16 인 자연수, 유니크
    8방향
상어: (0,0)물고기 먹으며 시작. (방향 동일)
이동 규칙
1. 번호작은 물고기부터
2. 이동가능: 빈칸, 물고기칸, 이동불가능: 상어칸, 격자외
    이동가능할때까지 반시계 회전한다.
    불가능하면 이동하지 않는다.
    이동시 물고기간 위치를 바꾼다.
3. 상어가 움직인다.
    방향에 있는 칸으로 얼마든 움직일수 있다.
    도착하는 칸의 물고기를 먹고, 방향을 갖는다.
    물고기가 없는 칸으로는 이동하지 않는다.
    이동할 칸이 없다면 집으로 간다.
출력
상어가 먹을 수 있는 물고기 번호의 합의 최대값?
'''

direction = {
    1: (-1, 0),
    2: (-1,-1),
    3: ( 0,-1),
    4: ( 1,-1),
    5: ( 1, 0),
    6: ( 1, 1),
    7: ( 0, 1),
    8: (-1, 1),
}
import sys
from pprint import pprint

# 테스트용
# sys.stdin = open('input.txt')
# T = 4
# debug = True

# 제출용
T = 1
debug = False

def fish_move(field, number): #field를 바꾼다.
    for r in range(4):
        for c in range(4):
            if field[r][c][0] == number:
                # 원래 방향부터 반시계방향으로 돌며 이동할 칸 탐색
                for dd in range(8):
                    d = (field[r][c][1] + dd)
                    d = d if d < 9 else d - 8 
                    nr, nc = r + direction[d][0], c + direction[d][1]
                    # print(field[nr][nc])
                    if 0<=nr<4 and 0<=nc<4 and field[nr][nc][0] >= 0: # -1은 상어, 0은 빈칸(물고기가 먹힌칸)
                        field[r][c], field[nr][nc] = field[nr][nc], (number,  d) # 회전하는 과정에서 방향 바뀐것 적용
                        return

def new_game(field, ndead, shark):
    global result
    # 1. 물고기 배치
    nfield = [field[i][:] for i in range(4)]
    for n in range(1, 16+1):
        if not ndead[n]:
            fish_move(nfield, n) # field가 직접 변경되는 작업임

    # 2. 상어 배치
    r, c, d = shark
    dr, dc = direction[d]
    nr, nc = r, c
    nr += dr
    nc += dc

    temp_sum = sum(ndead)
    if debug:                    
        pprint(nfield)

    while 0 <= nr < 4 and 0 <= nc < 4:
        if nfield[nr][nc][0] >= 1: # 1. 물고기칸
            number, head = nfield[nr][nc] # 물고기 번호, 방향

            new_field = [nfield[i][:] for i in range(4)]
            new_field[nr][nc] = (-1, head)
            new_field[r][c] = (0, 0)
            
            new_fish = ndead[:]
            new_fish[number] = number

            result = result if result >= temp_sum + number else temp_sum + number
            if debug:                    
                print(f'({nr},{nc}) {number}짜리 사냥성공 => 합:{temp_sum + number}')
                print()
            new_game(new_field, new_fish, (nr, nc, head))
        nr += dr
        nc += dc

for tc in range(1, T+1):
    field = []
    for _ in range(4):
        n1, d1, n2, d2, n3, d3, n4, d4 = map(int, input().split())
        field.append([(n1, d1), (n2, d2), (n3, d3), (n4, d4)])
    if debug: print(tc, "시작")
    

    # 상어 0,0 물고기 먹으며 시작
    dead = [0] * 17 # 물고기 생존여부
    number, head = field[0][0] # 물고기 번호, 방향
    dead[number] = number
    field[0][0] = (-1, head)
    # field[0][0] = (-1, head)

    result = number

    if debug:
        print("상어 사냥시작", number)

    new_game(field, dead, (0, 0, head)) # 필드, 죽은 물고기 리스트, 상어정보
    print(result)
    