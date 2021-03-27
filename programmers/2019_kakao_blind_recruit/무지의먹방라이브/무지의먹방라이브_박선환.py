def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    sorted_foods = sorted(food_times)
    max_foods = len(food_times)
    i = 0
    pre_food = 0
    current_k = 0
    while k >= current_k + (sorted_foods[i] - pre_food) * (max_foods - i):
        if sorted_foods[i] == pre_food:
            i += 1
            continue
        current_k += (sorted_foods[i] - pre_food) * (max_foods - i)
        pre_food = sorted_foods[i]
        i += 1
    
    k -= current_k
    food_times = list(map(lambda x: x - pre_food, food_times))

    index = -1
    while k > -1:
        index += 1
        index %= len(food_times)
        current_food = food_times[index]
        if current_food > 0:
            food_times[index] -= 1
            k -= 1

    return index + 1
    
'''
정확성 테스트
테스트 1 〉	통과 (0.01ms, 10.4MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.3MB)
테스트 4 〉	통과 (0.02ms, 10.2MB)
테스트 5 〉	통과 (0.02ms, 10.3MB)
테스트 6 〉	통과 (0.02ms, 10.2MB)
테스트 7 〉	통과 (0.02ms, 10.2MB)
테스트 8 〉	통과 (0.01ms, 10.2MB)
테스트 9 〉	통과 (0.02ms, 10.3MB)
테스트 10 〉	통과 (0.02ms, 10.3MB)
테스트 11 〉	통과 (0.02ms, 10.3MB)
테스트 12 〉	통과 (0.02ms, 10.2MB)
테스트 13 〉	통과 (0.02ms, 10.2MB)
테스트 14 〉	통과 (0.02ms, 10.2MB)
테스트 15 〉	통과 (0.02ms, 10.3MB)
테스트 16 〉	통과 (0.00ms, 10.3MB)
테스트 17 〉	통과 (0.02ms, 10.3MB)
테스트 18 〉	통과 (0.02ms, 10.3MB)
테스트 19 〉	통과 (0.00ms, 10.2MB)
테스트 20 〉	통과 (0.00ms, 10.3MB)
테스트 21 〉	통과 (0.07ms, 10.2MB)
테스트 22 〉	통과 (0.12ms, 10.4MB)
테스트 23 〉	통과 (0.00ms, 10.4MB)
테스트 24 〉	통과 (0.68ms, 10.2MB)
테스트 25 〉	통과 (0.85ms, 10.2MB)
테스트 26 〉	통과 (0.90ms, 10.3MB)
테스트 27 〉	통과 (1.07ms, 10.2MB)
테스트 28 〉	통과 (0.02ms, 10.3MB)
테스트 29 〉	통과 (0.02ms, 10.2MB)
테스트 30 〉	통과 (0.01ms, 10.2MB)
테스트 31 〉	통과 (0.01ms, 10.3MB)
테스트 32 〉	통과 (0.02ms, 10.3MB)

효율성 테스트
테스트 1 〉	실패 (시간 초과)
테스트 2 〉	실패 (시간 초과)
테스트 3 〉	실패 (시간 초과)
테스트 4 〉	실패 (시간 초과)
테스트 5 〉	실패 (시간 초과)
테스트 6 〉	실패 (시간 초과)
테스트 7 〉	실패 (시간 초과)
테스트 8 〉	실패 (시간 초과)
'''

# def solution(food_times, k):
#     # 더 섭취해야할 음식이 없는 경우
#     if sum(food_times) <= k:
#         return -1
#     # (남아있는 수 * 그 중 최솟값 m)이 k보다 작거나 같은 지 확인한다.
#     # m을 전체 원소를 돌면서 빼준다.
#     # 0이 된 값들을 100,000,001 처리하고, 남아있는 수를 업데이트 한다.
#     # 남아있는 수 * m을 k에서 빼준다. 이후 다시 반복
    
#     # 만약 while 조건에서 나왔을 때는, 그때부터 for 문 돌면서 최종 찾기
    
#     remain_nums = len(food_times)
#     min_value = min(food_times)
#     inf_value = max(food_times) + 1
#     while k and remain_nums * min_value <= k:
#         food_times = list(map(lambda x: inf_value if x == inf_value or x - min_value == 0 else x - min_value, food_times))
#         k -= remain_nums * min_value
#         remain_nums = len(list(filter(lambda x: x < inf_value, food_times)))
#         min_value = min(food_times)
    
#     i = -1
#     while k > -1:
#         i += 1
#         i %= len(food_times)
#         current_food = food_times[i]
#         if current_food != inf_value:
#             if current_food == 1:
#                 food_times[i] = inf_value
#             else:
#                 food_times[i] -= 1
#             k -= 1
#     return i + 1

'''
정확성 테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.02ms, 10.1MB)
테스트 3 〉	통과 (0.03ms, 10.3MB)
테스트 4 〉	통과 (0.03ms, 10.3MB)
테스트 5 〉	통과 (0.04ms, 10.1MB)
테스트 6 〉	통과 (0.04ms, 10.2MB)
테스트 7 〉	통과 (0.04ms, 10MB)
테스트 8 〉	통과 (0.04ms, 10.2MB)
테스트 9 〉	통과 (0.05ms, 10.2MB)
테스트 10 〉	통과 (0.06ms, 10.2MB)
테스트 11 〉	통과 (0.06ms, 10.3MB)
테스트 12 〉	통과 (0.06ms, 10.2MB)
테스트 13 〉	통과 (0.08ms, 10.3MB)
테스트 14 〉	통과 (0.06ms, 10.2MB)
테스트 15 〉	통과 (0.07ms, 10.1MB)
테스트 16 〉	통과 (0.00ms, 10.2MB)
테스트 17 〉	통과 (0.07ms, 10.2MB)
테스트 18 〉	통과 (0.07ms, 10.3MB)
테스트 19 〉	통과 (0.00ms, 10.2MB)
테스트 20 〉	통과 (0.00ms, 10.2MB)
테스트 21 〉	통과 (1.64ms, 10.2MB)
테스트 22 〉	통과 (2.11ms, 10.1MB)
테스트 23 〉	통과 (0.00ms, 10.2MB)
테스트 24 〉	통과 (6.91ms, 10.2MB)
테스트 25 〉	통과 (3.74ms, 10.3MB)
테스트 26 〉	통과 (14.96ms, 10.3MB)
테스트 27 〉	통과 (49.59ms, 10.4MB)
테스트 28 〉	통과 (0.05ms, 10.2MB)
테스트 29 〉	통과 (0.04ms, 10.2MB)
테스트 30 〉	통과 (0.01ms, 10.2MB)
테스트 31 〉	통과 (0.02ms, 10MB)
테스트 32 〉	통과 (0.02ms, 10.1MB)

효율성 테스트
테스트 1 〉	실패 (시간 초과)
테스트 2 〉	실패 (시간 초과)
테스트 3 〉	실패 (시간 초과)
테스트 4 〉	실패 (시간 초과)
테스트 5 〉	실패 (시간 초과)
테스트 6 〉	실패 (시간 초과)
테스트 7 〉	실패 (시간 초과)
테스트 8 〉	실패 (시간 초과)
'''