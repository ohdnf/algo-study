"""
상어 번호 1 ~ M
1번 상어가 가장 강력해서 나머지를 쫓아낼 수 있다.

N x N 크기의 격자
M개의 칸에 상어 한 마리씩

1초마다
1. 상어는 자신의 위치에 냄새를 뿌린다.
2. 모든 상어가 상하좌우로 이동

냄새는 k번 이동 후 사라짐

이동 우선순위
1. 아무 냄새가 없는 칸
2. 자신의 냄새가 있는 칸
3. 가능한 칸 중 주어진 방향 우선순위를 따른다.
"""
import heapq

N, M, k = map(int, input().split())
init = [list(map(int, input().split())) for _ in range(N)]
init_dir = list(map(int, input().split()))
init_dir.insert(0, 0)

dir_priority = [{1: [], 2: [], 3: [], 4: []}]   # 상어 번호 / 상어 현재 방향 / 우선 순위 방향 네 가지
for _ in range(M):
    dp = {
        1: list(map(int, input().split())),
        2: list(map(int, input().split())),
        3: list(map(int, input().split())),
        4: list(map(int, input().split()))
    }
    dir_priority.append(dp)

direction = ((), (-1, 0), (1, 0), (0, -1), (0, 1))  # 상, 하, 좌, 우

shark = [[list() for _ in range(N)] for _ in range(N)]
smell = [[list() for _ in range(N)] for _ in range(N)]
count = 0
for row in range(N):
    for col in range(N):
        if init[row][col]:
            count += 1
            # init_num = init[row][col] - 1
            init_num = init[row][col]
            shark[row][col].append([init_num, init_dir[init_num]])   # 상어 번호, 상어의 방향

time = 0
while count > 1 and time <= 1000:
    temp = [[list() for _ in range(N)] for _ in range(N)]   # 상어 이동 후 임시 저장
    # 냄새 남기고 이동하기
    for row in range(N):
        for col in range(N):
            # 상어 이동
            if shark[row][col]:
                shark_num, shark_dir = shark[row][col].pop()
                smell[row][col] = [shark_num, k]     # 냄새 뿌리기: [상어 번호, 냄새 유지 시간]
                # 냄새가 없는 칸 중 이동할 칸 찾기
                for priority_dir in dir_priority[shark_num][shark_dir]:
                    nrow, ncol = row + direction[priority_dir][0], col + direction[priority_dir][1]
                    if 0 <= nrow < N and 0 <= ncol < N and not smell[nrow][ncol]:
                        heapq.heappush(temp[nrow][ncol], [shark_num, priority_dir])
                        # shark[nrow][ncol].append([shark_num, priority_dir])
                        break
                # 없으면 자신의 냄새가 있는 칸 중 이동할 칸 찾기
                else:
                    for priority_dir in dir_priority[shark_num][shark_dir]:
                        nrow, ncol = row + direction[priority_dir][0], col + direction[priority_dir][1]
                        if 0 <= nrow < N and 0 <= ncol < N and smell[nrow][ncol][0] == shark_num:
                            heapq.heappush(temp[nrow][ncol], [shark_num, priority_dir])
                            # shark[nrow][ncol].append([shark_num, priority_dir])
                            break

    for row in range(N):
        for col in range(N):
            # 냄새 감소 처리
            if smell[row][col]:
                smell[row][col][1] -= 1
                if smell[row][col][1] == 0:
                    smell[row][col].clear()
            # 같은 칸 두 마리 이상 상어들 처리
            if len(temp[row][col]) > 1:
                last_shark_num, last_shark_dir = heapq.heappop(temp[row][col])
                count -= len(temp[row][col])
                temp[row][col].clear()
                heapq.heappush(temp[row][col], [last_shark_num, last_shark_dir])
    shark = temp
    time += 1
    # print(time, "초 후 현재 상어 수:", count)
    # for line in shark:
    #     print(line)
    # print()
    # print("냄새")
    # for line in smell:
    #     print(line)
    # print("-" * 30)

if time > 1000:
    print(-1)
else:
    print(time)

"""
Python3
Memory 31400 KB
Time 580 ms
"""