from collections import deque


def solution(food_times, k):
    t = 0   # t: 현재까지 소요된 시간
    table = deque()
    # 첫 번째 순회
    for idx, food in enumerate(food_times):
        # 네트워크 장애가 발생할 경우
        if t == k:
            return idx + 1    # [idx+1] 번째 음식을 섭취할 차례
        # [idx+1] 번째 음식을 1초 동안 섭취
        if food != 1:
            # 음식이 남을 경우 회전판에 다시 올려놓기(음식번호, 남은시간)
            table.append([idx + 1, food - 1])
        t += 1
    # 첫 번째 이후 순회
    while table and t < k:
        curr_idx, curr_food = table.popleft()
        if curr_food != 1:
            table.append([curr_idx, curr_food - 1])
        t += 1
    if not table:
        return -1
    return table[0][0]

"""
채점 결과
정확성: 42.9
효율성: 0.0
합계: 42.9 / 100.0
"""

