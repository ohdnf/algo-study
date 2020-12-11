'''
- 초기 크기 2
- 1초에 상하좌우로 인접한 한 칸씩 이동
- 자신의 크기보다 큰 물고기가 있는 칸은 지나갈 수 없고, 
- 자신의 크기보다 작은 물고기만 먹을 수 있다.
=> 크기가 같은 물고기 = 지나가기 (o), 먹기 (x)

먹을 수 있는 물고기가 공간에 없다면? - 엄마 상어에게 도움 요청
먹을 수 있는 물고기 1마리 - 먹는다!
먹을 수 있는 물고기 2마리 이상?
- 거리는 먹으러 갈 때 "지나가야 하는 칸의 개수 최솟값"
- 거리가 가까운 물고기가 많다면, "가장 위에 있는 물고기" (이런 물고기 여러마리라면, 가장 "왼쪽에 있는 물고기")

이동은 1초!! & 먹는 시간 0초!
물고기를 먹으면 빈칸

엄마 상어에게 도움을 요청하지 않고, 물고기가 잡아먹을 수 있는 시간을 구하라 

0: 빈 칸
1, 2, 3, 4, 5, 6: 칸에 있는 물고기의 크기
9: 아기 상어 위치 

- 자신의 크기와 같은 수의 물고기를 먹을 때 마다 크기가 1 증가 
'''
from collections import deque

di = [0, 0, 1, -1]
dj = [-1, 1, 0, 0]

# shark (size, position, eaten)
def eat():
    global time, shark, arr
    shark_pos = shark[1]
    q = deque()
    q.append(shark_pos) 
    visited = [[0] * N for _ in range(N)]
    visited[shark_pos[0]][shark_pos[1]] = True 
    distance = 0
    fishes = []

    while q:
        distance += 1
        # for문을 돌았을 때 queue의 길이만큼 돌면, 거리가 1씩 증가하는 방식! 
        # 즉 여기서 여러마리가 존재한다고 해도, 거리가 같다.
        for _ in range(len(q)):
            i, j = q.popleft() 
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k] 
                if ni < 0 or ni >= N or nj < 0 or nj >= N:
                    continue
                # 상어의 사이즈보다 같거나 작고, 방문하지 않았다면 지나가기 가능
                if arr[ni][nj] <= shark[0] and visited[ni][nj] == False:
                    visited[ni][nj] = True
                    # 상어의 사이즈보다 작아야 먹기가 가능 
                    if 0 < arr[ni][nj] < shark[0]:
                        fishes.append((ni, nj))
                    else: 
                        q.append((ni, nj))
        # 돌았을 때 섭취 가능한 물고기가 있다면 break
        if fishes:
            break
    # 섭취 가능한 물고기가 있다면 
    if fishes:
        # 물고기 먼저 sorting 하기 
        fishes = sorted(fishes, key = lambda x: (x[0], x[1]))
        arr[fishes[0][0]][fishes[0][1]] = 9
        arr[shark_pos[0]][shark_pos[1]] = 0
        # 상어의 위치를 현재 먹이물고기 위치로 변경
        shark[1] = fishes[0]
        # 몇 개 먹었는지 eaten 카운트 1 추가 
        shark[2] += 1
        # 만약 상어 크기와 먹은 갯수가 같다면, 상어 크기 1 추가/ 먹은 갯수 리셋
        if shark[2] == shark[0]:
            shark[0] += 1
            shark[2] = 0
        # 걸린 시간에 거리만큼 추가하기 
        time += distance 
        return True
    else:
        return False 

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

time = 0
size = 2
eaten = 0

for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            # shark의 크기, 위치, 갯수
            shark = [2, (i, j), 0]
            shark_loc = [i, j]
            arr[i][j] = 0

while True:
    if eat() == False:
        break

print(time)