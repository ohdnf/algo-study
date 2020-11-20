# 첫 번째 솔루션
def solution(stones, k):
    answer = 0
    R = range(len(stones))
    breaking = True
    while breaking:
        temp = 0
        for i in R:
            if stones[i]:
                stones[i] -= 1
                temp = 0
            else:
                temp += 1
                if temp >= k:
                    breaking = False
                    break
        else:
            answer += 1
                
    return answer

#-----------------------------------
# 정확성 테스트
# 테스트 1 〉	통과 (0.01ms, 10.2MB)
# 테스트 2 〉	통과 (0.01ms, 10.2MB)
# 테스트 3 〉	통과 (0.02ms, 10.2MB)
# 테스트 4 〉	통과 (0.10ms, 10.2MB)
# 테스트 5 〉	통과 (0.06ms, 10.1MB)
# 테스트 6 〉	통과 (26.76ms, 10.2MB)
# 테스트 7 〉	통과 (75.83ms, 10.2MB)
# 테스트 8 〉	통과 (80.37ms, 10.1MB)
# 테스트 9 〉	통과 (90.17ms, 10.2MB)
# 테스트 10 〉	통과 (0.12ms, 10.2MB)
# 테스트 11 〉	통과 (0.04ms, 10.2MB)
# 테스트 12 〉	통과 (0.21ms, 10.2MB)
# 테스트 13 〉	통과 (1.16ms, 10.3MB)
# 테스트 14 〉	통과 (27.03ms, 10.2MB)
# 테스트 15 〉	통과 (74.30ms, 10.2MB)
# 테스트 16 〉	통과 (80.67ms, 10.2MB)
# 테스트 17 〉	통과 (84.60ms, 10.2MB)
# 테스트 18 〉	통과 (0.09ms, 10.2MB)
# 테스트 19 〉	통과 (0.86ms, 10.1MB)
# 테스트 20 〉	통과 (2.02ms, 10.2MB)
# 테스트 21 〉	통과 (23.25ms, 10.3MB)
# 테스트 22 〉	통과 (58.07ms, 10.2MB)
# 테스트 23 〉	통과 (81.83ms, 10.2MB)
# 테스트 24 〉	통과 (81.79ms, 10.1MB)
# 테스트 25 〉	통과 (0.01ms, 10.2MB)
#-----------------------------------
# 효율성 테스트
# 테스트 1 〉	실패 (시간 초과)
# 테스트 2 〉	실패 (시간 초과)
# 테스트 3 〉	실패 (시간 초과)
# 테스트 4 〉	실패 (시간 초과)
# 테스트 5 〉	실패 (시간 초과)
# 테스트 6 〉	실패 (시간 초과)
# 테스트 7 〉	실패 (시간 초과)
# 테스트 8 〉	실패 (시간 초과)
# 테스트 9 〉	실패 (시간 초과)
# 테스트 10 〉	실패 (시간 초과)
# 테스트 11 〉	실패 (시간 초과)
# 테스트 12 〉	실패 (시간 초과)
# 테스트 13 〉	실패 (시간 초과)
# 테스트 14 〉	실패 (시간 초과)
#-----------------------------------
# 정확성: 64.1
# 효율성: 0.0
# 합계: 64.1 / 100.0

##############################################
##############################################
##############################################

# 두 번째 솔루션
def solution(stones, k):
    answer = max(stones)
    
    for i in range(len(stones) - (k+1)):
        limit = stones[i+k+1]
        max_score = 0
        for j in range(1, k+1):
            c_stone = stones[i+j]
            if c_stone > limit:
                break
            else:
                if c_stone > max_score:
                    max_score = c_stone
        else:
            if answer > max_score:
                answer = max_score
            
    return answer

#-----------------------------------
# 정확성 테스트
# 테스트 1 〉	통과 (0.00ms, 10.2MB)
# 테스트 2 〉	통과 (0.01ms, 10.2MB)
# 테스트 3 〉	실패 (0.01ms, 10.2MB)
# 테스트 4 〉	통과 (0.03ms, 10.2MB)
# 테스트 5 〉	통과 (0.06ms, 10.2MB)
# 테스트 6 〉	통과 (0.36ms, 10.2MB)
# 테스트 7 〉	통과 (0.90ms, 10.2MB)
# 테스트 8 〉	통과 (1.00ms, 10.2MB)
# 테스트 9 〉	통과 (1.07ms, 10.2MB)
# 테스트 10 〉	통과 (0.06ms, 10.1MB)
# 테스트 11 〉	통과 (0.01ms, 10.1MB)
# 테스트 12 〉	통과 (0.03ms, 10.3MB)
# 테스트 13 〉	통과 (0.07ms, 10.2MB)
# 테스트 14 〉	통과 (0.42ms, 10.3MB)
# 테스트 15 〉	통과 (0.90ms, 10.2MB)
# 테스트 16 〉	통과 (1.06ms, 10.2MB)
# 테스트 17 〉	통과 (1.01ms, 10.2MB)
# 테스트 18 〉	통과 (0.01ms, 10.1MB)
# 테스트 19 〉	통과 (0.03ms, 10.2MB)
# 테스트 20 〉	통과 (0.07ms, 10.2MB)
# 테스트 21 〉	통과 (0.39ms, 10.3MB)
# 테스트 22 〉	통과 (0.96ms, 10.2MB)
# 테스트 23 〉	통과 (1.02ms, 10.3MB)
# 테스트 24 〉	통과 (1.10ms, 10.2MB)
# 테스트 25 〉	통과 (0.03ms, 10.2MB)
#-----------------------------------
# 효율성 테스트
# 테스트 1 〉	통과 (202.60ms, 18.7MB)
# 테스트 2 〉	통과 (205.71ms, 18.6MB)
# 테스트 3 〉	통과 (212.27ms, 18.5MB)
# 테스트 4 〉	실패 (시간 초과)
# 테스트 5 〉	실패 (시간 초과)
# 테스트 6 〉	실패 (시간 초과)
# 테스트 7 〉	통과 (201.20ms, 18.6MB)
# 테스트 8 〉	통과 (139.22ms, 18.6MB)
# 테스트 9 〉	통과 (203.59ms, 18.5MB)
# 테스트 10 〉	통과 (128.50ms, 18.5MB)
# 테스트 11 〉	통과 (201.31ms, 18.6MB)
# 테스트 12 〉	통과 (143.11ms, 18.6MB)
# 테스트 13 〉	실패 (58.60ms, 18.6MB)
# 테스트 14 〉	실패 (시간 초과)
#-----------------------------------
# 정확성: 61.5
# 효율성: 23.1
# 합계: 84.6 / 100.0
#-----------------------------------