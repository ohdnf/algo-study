def solution(food_times, k):
    # e.g. food_times = [ 105, 105, 3, 2, 2], k = 214
    from collections import defaultdict
    
    # 예외 처리
    if sum(food_times) <= k:
        return -1
    N = len(food_times)
    
    # food_time_dict: {105:2, 3:1, 2:2}
    # food_time_sorted_keys: [2, 3, 105]
    food_time_dict = defaultdict(int) # 각 음식량을 카운팅
    for food_time in food_times:
        food_time_dict[food_time] += 1
    
    food_time_sorted_keys = sorted(list(food_time_dict.keys())) # 음식량 낮은것부터
    
    prev_amount = 0 # 최근 계산에 활용한 amount
    remain = N # amount번 순회때, 남은 음식 갯수
    
    for amount in food_time_sorted_keys: # amount번째 순회
        
        # if문 : amount번 순회에 이르기전, k < 0 이 되어 break
            # 이문제는 다음에 먹을 차례의 음식이여서 k <= 0 아닌 k < 0 (딱 맞으면, 다음에 먹을 음식 X => return -1)
            # 만약 마지막에 먹을 문제를 고르는 것이라면 k <= 0
        # 1. amount=2 => 214 > (2-0) * 5
        # 2. amount=3 => 204 > (3-2) * 3
        # 3. amount=105 => 201 < (105-3) * 2
            # break => 현재 amount=105, k=201, remain=2 보존중
        if k < (amount-prev_amount) * remain:
            break
        
        k -= (amount-prev_amount) * remain
        # 1. k: 214 -= (2-0) * 5
        # 2. k: 204 -= (3-2) * 3
        
        remain -= food_time_dict[amount] # 이번 순회로 사라진 음식 갯수 빼줌
        # 1. remain: 5 -= 2 (음식량 2짜리 음식 갯수: 2)
        # 2. remain: 3 -= 1 (음식량 3짜리 음식 갯수: 1)
        
        prev_amount = amount
        # 1. 0 => 2
        # 2. 2 => 3
    
    # 3. amount=105, k=201, remain=2 
    k %= remain
    # 3. 201 %= 2
        # k = 201 vs k = 1
        # 만약이게 없다면. (남은 음식을 순회하는)반복문을 (200//2)100번 더 반복
    for index, food_time in enumerate(food_times):
        
        # 3. food_times [105, 105, 3, 2, 2] 에서 3,2개짜리 음식은 현재 없어진 상태. food_time=3 or 2는 무시
        if food_time < amount:
            continue
        
        # 3-1. index=0, food_time=105, k=1
        # 3-2. index=1, food_time=105, k=0 (return 1+1)
        if k == 0:
            return index+1
        k -= 1
        # 3-1. 1-=1

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
