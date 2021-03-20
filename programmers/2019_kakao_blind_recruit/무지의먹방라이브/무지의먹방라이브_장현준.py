def solution(food_times, k):
    from collections import defaultdict
    
    # 예외 처리
    if sum(food_times) <= k:
        return -1
    N = len(food_times)
    
    food_time_dict = defaultdict(int) # 각 음식량을 카운팅
    for food_time in food_times:
        food_time_dict[food_time] += 1
    
    food_time_sorted_keys = sorted(list(food_time_dict.keys())) # 음식량 낮은것부터
    
    prev_amount = 0 # 최근에 계산에 활용한 amount
    remain = N # amount번 순회때, 남은 음식 갯수
    
    for amount in food_time_sorted_keys: # amount번째 순회
        if k < (amount-prev_amount) * remain: # amount번째 순회 끝나기 이전에 k = 0 도달
            break
        k -= (amount-prev_amount) * remain # (amount - 이전 amount) * 남아있던 음식 갯수
        remain -= food_time_dict[amount] # 이번 순회로 사라진 음식 갯수 빼줌
        prev_amount = amount
    
    # amount, k 보존
    k %= remain # e.g. [1, 2, 4, 5, 6] , amount=4 & remain=3 & k=5 => k % remain == 5 % 3 == 2 
    for index, food_time in enumerate(food_times):
        if food_time < amount: # e.g. 1, 2는 무시하고 지나감
            continue
        if k == 0:
            return index+1
        k -= 1

'''
정확성  테스트
테스트 1 〉	통과 (0.02ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.02ms, 10.2MB)
테스트 4 〉	통과 (0.02ms, 10.2MB)
테스트 5 〉	통과 (0.02ms, 10.2MB)
테스트 6 〉	통과 (0.02ms, 10.2MB)
테스트 7 〉	통과 (0.02ms, 10.2MB)
테스트 8 〉	통과 (0.02ms, 10.1MB)
테스트 9 〉	통과 (0.02ms, 10.2MB)
테스트 10 〉통과 (0.02ms, 10.2MB)
테스트 11 〉통과 (0.02ms, 10.2MB)
테스트 12 〉통과 (0.02ms, 10.2MB)
테스트 13 〉통과 (0.02ms, 10.2MB)
테스트 14 〉통과 (0.02ms, 10.2MB)
테스트 15 〉통과 (0.02ms, 10.1MB)
테스트 16 〉통과 (0.00ms, 10.2MB)
테스트 17 〉통과 (0.02ms, 10.2MB)
테스트 18 〉통과 (0.02ms, 10.2MB)
테스트 19 〉통과 (0.00ms, 10.2MB)
테스트 20 〉통과 (0.00ms, 10.2MB)
테스트 21 〉통과 (0.05ms, 10.1MB)
테스트 22 〉통과 (0.08ms, 10.2MB)
테스트 23 〉통과 (0.00ms, 10.2MB)
테스트 24 〉통과 (0.28ms, 10.2MB)
테스트 25 〉통과 (0.79ms, 10.3MB)
테스트 26 〉통과 (0.39ms, 10.2MB)
테스트 27 〉통과 (0.97ms, 10.3MB)
테스트 28 〉통과 (0.02ms, 10.2MB)
테스트 29 〉통과 (0.02ms, 10.1MB)
테스트 30 〉통과 (0.01ms, 10.2MB)
테스트 31 〉통과 (0.01ms, 10.3MB)
테스트 32 〉통과 (0.03ms, 10.1MB)

효율성  테스트
테스트 1 〉	통과 (129.41ms, 33.7MB)
테스트 2 〉	통과 (46.29ms, 18.6MB)
테스트 3 〉	통과 (112.45ms, 26.3MB)
테스트 4 〉	통과 (33.78ms, 18.6MB)
테스트 5 〉	통과 (97.96ms, 26.3MB)
테스트 6 〉	통과 (59.89ms, 22.3MB)
테스트 7 〉	통과 (69.78ms, 22.4MB)
테스트 8 〉	통과 (26.34ms, 18.6MB)
채점 결과
정확성: 42.9
효율성: 57.1
합계: 100.0 / 100.0
'''