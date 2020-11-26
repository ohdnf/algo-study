# 첫 번째 풀이
def solution(k, room_number):
    answer = []
    visited = [0]*(k+1)
    for num in room_number:
        while True:
            if not visited[num]:
                answer.append(num)
                visited[num] = 1
                break
            num += 1
    return answer

'''
정확성 테스트
테스트 1 〉	통과 (0.00ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.21ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.1MB)
테스트 6 〉	통과 (0.02ms, 10.2MB)
테스트 7 〉	통과 (0.01ms, 10.2MB)
테스트 8 〉	통과 (0.00ms, 10.2MB)
테스트 9 〉	통과 (0.01ms, 10.1MB)
테스트 10 〉	통과 (0.01ms, 10.1MB)
테스트 11 〉	통과 (0.01ms, 10.2MB)
테스트 12 〉	통과 (0.01ms, 10.2MB)
테스트 13 〉	통과 (0.01ms, 10.1MB)
테스트 14 〉	통과 (0.01ms, 10.2MB)
테스트 15 〉	통과 (0.03ms, 10.2MB)
테스트 16 〉	통과 (0.04ms, 10MB)
테스트 17 〉	통과 (0.04ms, 10.2MB)
테스트 18 〉	통과 (0.12ms, 10.2MB)
테스트 19 〉	통과 (0.26ms, 10.2MB)
테스트 20 〉	통과 (0.34ms, 10.3MB)
테스트 21 〉	통과 (1.20ms, 10.3MB)
테스트 22 〉	통과 (0.99ms, 10.2MB)
테스트 23 〉	통과 (0.22ms, 10.3MB)
테스트 24 〉	통과 (0.95ms, 10.3MB)
테스트 25 〉	통과 (0.02ms, 10.2MB)
테스트 26 〉	통과 (0.10ms, 10.2MB)

효율성 테스트
테스트 1 〉	실패 (시간 초과)
테스트 2 〉	실패 (시간 초과)
테스트 3 〉	실패 (시간 초과)
테스트 4 〉	실패 (시간 초과)
테스트 5 〉	실패 (런타임 에러)
테스트 6 〉	실패 (런타임 에러)
테스트 7 〉	실패 (런타임 에러)
'''

###############################

# 두 번째 풀이
def solution(k, room_number):
    answer = []
    rooms = list(range(k+1))
    visited = [0]*(k+1)
    for num in room_number:
        if not visited[num]:
            answer.append(num)
            visited[num] = 1
            rooms.remove(num)
        else:
            for n in rooms:
                if n > num:
                    num = n
                    break
            answer.append(num)
            visited[num] = 1
            rooms.remove(num)
    return answer

'''
정확성 테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.3MB)
테스트 3 〉	통과 (0.01ms, 10.1MB)
테스트 4 〉	통과 (0.06ms, 10.3MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.04ms, 10.2MB)
테스트 7 〉	통과 (0.02ms, 10.2MB)
테스트 8 〉	통과 (0.01ms, 10.2MB)
테스트 9 〉	통과 (0.01ms, 10.1MB)
테스트 10 〉	통과 (0.01ms, 10.2MB)
테스트 11 〉	통과 (0.01ms, 10.2MB)
테스트 12 〉	통과 (0.03ms, 10.2MB)
테스트 13 〉	통과 (0.02ms, 10.3MB)
테스트 14 〉	통과 (0.03ms, 10.2MB)
테스트 15 〉	통과 (0.27ms, 10.2MB)
테스트 16 〉	통과 (0.39ms, 10.2MB)
테스트 17 〉	통과 (1.20ms, 10.2MB)
테스트 18 〉	통과 (2.74ms, 10.2MB)
테스트 19 〉	통과 (5.25ms, 10.3MB)
테스트 20 〉	통과 (7.48ms, 10.3MB)
테스트 21 〉	통과 (13.68ms, 10.3MB)
테스트 22 〉	통과 (15.44ms, 10.3MB)
테스트 23 〉	통과 (14.12ms, 10.1MB)
테스트 24 〉	통과 (20.94ms, 10.3MB)
테스트 25 〉	통과 (0.02ms, 10.3MB)
테스트 26 〉	통과 (0.03ms, 10.2MB)

효율성 테스트
테스트 1 〉	실패 (시간 초과)
테스트 2 〉	실패 (시간 초과)
테스트 3 〉	실패 (시간 초과)
테스트 4 〉	실패 (시간 초과)
테스트 5 〉	실패 (런타임 에러)
테스트 6 〉	실패 (런타임 에러)
테스트 7 〉	실패 (런타임 에러)
'''

############################

#세 번째 풀이
def solution(k, room_number):
    answer = []
    visited = [0]*(k+2)
    for num in room_number:
        if not visited[num]:
            answer.append(num)
            next_num = num + 1
            temp = []
            while True:
                if not visited[next_num]:
                    for n in temp:
                        visited[n] = next_num
                    visited[num] = next_num
                    break
                else:
                    temp.append(next_num)
                    next_num = visited[next_num]                    
        else:
            done = True
            temp = []
            while done:
                temp.append(num)
                num = visited[num]
                if not visited[num]:
                    answer.append(num)
                    next_num = num + 1
                    while True:
                        if not visited[next_num]:
                            for n in temp:
                                visited[n] = next_num
                            visited[num] = next_num
                            done = False
                            break
                        else:
                            temp.append(next_num)
                            next_num = visited[next_num]
            
    return answer

'''
정확성 테스트
테스트 1 〉	통과 (0.00ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.08ms, 10.3MB)
테스트 5 〉	통과 (0.01ms, 10.3MB)
테스트 6 〉	통과 (0.02ms, 10.2MB)
테스트 7 〉	통과 (0.02ms, 10.3MB)
테스트 8 〉	통과 (0.01ms, 10.2MB)
테스트 9 〉	통과 (0.01ms, 10.1MB)
테스트 10 〉	통과 (0.01ms, 10.3MB)
테스트 11 〉	통과 (0.01ms, 10.2MB)
테스트 12 〉	통과 (0.02ms, 10MB)
테스트 13 〉	통과 (0.01ms, 10.3MB)
테스트 14 〉	통과 (0.02ms, 10.1MB)
테스트 15 〉	통과 (0.05ms, 10.2MB)
테스트 16 〉	통과 (0.06ms, 10.3MB)
테스트 17 〉	통과 (0.06ms, 10.3MB)
테스트 18 〉	통과 (0.15ms, 10MB)
테스트 19 〉	통과 (0.28ms, 10.1MB)
테스트 20 〉	통과 (0.35ms, 10.3MB)
테스트 21 〉	통과 (0.63ms, 10.2MB)
테스트 22 〉	통과 (0.78ms, 10.3MB)
테스트 23 〉	통과 (0.60ms, 10.3MB)
테스트 24 〉	통과 (0.83ms, 10.2MB)
테스트 25 〉	통과 (0.02ms, 10.1MB)
테스트 26 〉	통과 (0.05ms, 10.2MB)

효율성 테스트
테스트 1 〉	통과 (210.11ms, 42.8MB)
테스트 2 〉	통과 (231.34ms, 38.4MB)
테스트 3 〉	통과 (254.01ms, 49MB)
테스트 4 〉	통과 (223.48ms, 49.7MB)
테스트 5 〉	실패 (런타임 에러)
테스트 6 〉	실패 (런타임 에러)
테스트 7 〉	실패 (런타임 에러)
'''