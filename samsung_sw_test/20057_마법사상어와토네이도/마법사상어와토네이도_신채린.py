# import sys
# sys.stdin = open('마법사 상어와 토네이도.txt')

# N = int(input())
# arr = [list(map(int, input().split()) for _ in range(N)]

# wind = [
#     # 위쪽
#     [-1, 0, 7%],
#     [-2, 0, 2%],
#     [-1, 1, 1%],
#     [-1, -1, 10%],
#     [0, -2, 5%],
#     [1, 0, 7%],
#     [-1, -1, 10%],
#     [1, 1, 1%],
#     [2, 0, 2%]
# ]


# cnt = 1

sand_dx = [[-1, -1, -2, -1, 0, 1, 1, 2, 1], [-1, 0, 0, 1, 2, 1, 0, 0, -1], [-1, -1, -2, -1, 0, 1, 1, 2, 1],
           [1, 0, 0, -1, -2, -1, 0, 0, 1]]
sand_dy = [[1, 0, 0, -1, -2, -1, 0, 0, 1], [-1, -1, -2, -1, 0, 1, 1, 2, 1], [-1, 0, 0, 1, 2, 1, 0, 0, -1],
           [-1, -1, -2, -1, 0, 1, 1, 2, 1]]
sand_value = [1, 7, 2, 10, 5, 10, 7, 2, 1]
last_sand = [[0, -1], [1, 0], [0, 1], [-1, 0]]

def tornado_with_sand(s_map, x, y, d, result):
    total_sand = s_map[x][y]
    move_sand = 0
    if total_sand != 0:
        for i in range(9):
            sand_x, sand_y = x + sand_dx[d][i], y + sand_dy[d][i]
            if 0 <= sand_x < N and 0 <= sand_y < N:
                s_map[sand_x][sand_y] += int(total_sand * (0.01 * sand_value[i]))
                move_sand += int(total_sand * (0.01 * sand_value[i]))
            else:
                result += int(total_sand * (0.01 * sand_value[i]))
                move_sand += int(total_sand * (0.01 * sand_value[i]))

    sand_x, sand_y = x + last_sand[d][0], y + last_sand[d][1]
    if 0 <= sand_x < N and 0 <= sand_y < N:
        s_map[sand_x][sand_y] += total_sand - move_sand
    else:
        result += total_sand - move_sand

    s_map[x][y] = 0
    return s_map, result


dx = [0, 1, 0, -1]  # 좌하우상
dy = [-1, 0, 1, 0]
N = int(input())
sand_map = [list(map(int, input().split())) for _ in range(N)]

tornado_length = 1
d, cnt, result = 0, 0, 0
tornado = [N//2, N//2]
while True:
    if cnt != 0 and cnt % 2 == 0:
        tornado_length += 1
    length = tornado_length
    while length > 0:
        start_x, start_y = tornado[0], tornado[1]
        next_x, next_y = start_x + dx[d], start_y + dy[d]
        sand_map, result = tornado_with_sand(sand_map, next_x, next_y, d, result)
        length -= 1
        tornado = [next_x, next_y]
        if tornado == [0, 0]:
            break
    cnt += 1
    d = (d+1) % 4
    if tornado == [0, 0]:
        break
print(result)