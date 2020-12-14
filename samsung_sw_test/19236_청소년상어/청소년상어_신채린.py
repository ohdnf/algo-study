# 물고기 이동
# 물고기는 번호가 작은 물고기부터 순서대로 이동
# 물고기는 한 칸 이동 
# 이동할 수 있는 칸 = 다른 '물고기 있는' 칸 + 빈 칸
# 이동할 수 없는 칸 = 상어 존재 + 공간 경계 넘는 칸 
# 방향을 이동할 수 있을 때까지 방향을 45도 반시계 회전 
from copy import deepcopy

direction = {
    1: [-1, 0],
    2: [-1, -1],
    3: [0, -1],
    4: [1, -1],
    5: [1, 0],
    6: [1, 1],
    7: [0, 1],
    8: [-1, 1]
}

def move_shark(i, j, direct, eaten):
    global arr, ans, direction
    backup = deepcopy(arr)
    move_fish()
    if ans < sum(eaten):
        ans = sum(eaten)
    for k in range(1, 4):
        # 상어의 새로운 좌표 찾기
        ni = i + direction[direct][0] * k
        nj = j + direction[direct][1] * k
        # 물고기가 없다면 스킵하기
        if 0 <= ni < 4 and 0 <= nj < 4:
            if arr[ni][nj][0] == 0:
                continue
            # eaten.append(backup[ni][nj][0]
            fish = arr[ni][nj][0]
            direct = arr[ni][nj][1]
            store = arr[i][j][1]
            arr[i][j][0] = 0
            arr[ni][nj][0] = -1
            move_shark(ni, nj, arr[ni][nj][1], eaten + [fish])
            # 물고기 원상태로 되돌려놓기 
            arr[i][j][0] = -1
            arr[ni][nj][0] = fish
            direct = store # ㅎ... 방향땜에 얼마나 헤맸나 ^0^
    # 맵 이전으로 돌려놓기
    arr = backup

    

def move_fish():
    for k in range(1, 17):
        # 먼저 해당 fish의 location을 찾는다 
        flag = False
        if k in eaten:
            continue
        for i in range(4):
            for j in range(4):
                if arr[i][j][0] == k:
                    fish_i = i
                    fish_j = j
                    fish_direction = arr[i][j][1]
                    flag = True
                    break
            if flag:
                break
        else:
            continue
        
        # 물고기가 이동할 수 있는지 확인해본다.
        while True:
            ni = fish_i + direction[fish_direction][0] 
            nj = fish_j + direction[fish_direction][1]
            if 0 <= ni < 4 and 0 <= nj < 4 and arr[ni][nj][0] != -1:
                temp_fish = arr[ni][nj]
                arr[ni][nj] = arr[fish_i][fish_j] 
                arr[fish_i][fish_j] = temp_fish
                break
            else:
                # 만약 이동할 수 없다면 이동 방향을 1 추가한다.
                fish_direction +=1 
                if fish_direction > 8:
                    fish_direction = fish_direction % 8
                arr[fish_i][fish_j][1] = fish_direction

arr = []
# 처음에 배열 만들기
for i in range(4):
    list1 = []
    temp = list(map(int, input().split()))
    for j in range(4):
        list1.append([temp[2*j], temp[2*j+1]])
    arr.append(list1)

# 상어가 뭐 먹었는지 체크하기 
eaten = []
eaten.append( arr[0][0][0])
ans = 0

# 상어 위치 바꾸기 
arr[0][0][0] = -1
shark_i = 0
shark_j = 0 
shark_dir = arr[0][0][1]

move_shark(shark_i, shark_j, shark_dir, eaten)


print(ans)

# 메모리: 29956 KB
# 시간: 88ms