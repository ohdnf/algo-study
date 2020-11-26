def solution(k, room_number):
    #k=방의개수
    #room_number=원하는 방번호 
    answer = []
    reserve = dict()
    for room in room_number:
        if room in reserve:
            # keys
            not_empty=list(reserve.keys())
            next = reserve[room]
            while True:
                if next not in not_empty:
                    answer.append(next)
                    reserve[next] = next + 1
                    break
                else:
                    next += 1
            
        else: 
            answer.append(room)
            reserve[room] = room + 1
    
    return answer

# 채점을 시작합니다.
# 정확성  테스트
# 테스트 1 〉	통과 (0.00ms, 10.3MB)
# 테스트 2 〉	통과 (0.01ms, 10.2MB)
# 테스트 3 〉	통과 (0.01ms, 10.2MB)
# 테스트 4 〉	통과 (1.92ms, 10.2MB)
# 테스트 5 〉	통과 (0.01ms, 10.1MB)
# 테스트 6 〉	통과 (0.05ms, 10.2MB)
# 테스트 7 〉	통과 (0.04ms, 10.2MB)
# 테스트 8 〉	통과 (0.01ms, 10.2MB)
# 테스트 9 〉	통과 (0.01ms, 10.2MB)
# 테스트 10 〉	통과 (0.01ms, 10.1MB)
# 테스트 11 〉	통과 (0.01ms, 10.2MB)
# 테스트 12 〉	통과 (0.03ms, 10.2MB)
# 테스트 13 〉	통과 (0.02ms, 10.2MB)
# 테스트 14 〉	통과 (0.02ms, 10.2MB)
# 테스트 15 〉	통과 (0.15ms, 10.2MB)
# 테스트 16 〉	통과 (0.36ms, 10.1MB)
# 테스트 17 〉	통과 (0.30ms, 10.2MB)
# 테스트 18 〉	통과 (1.53ms, 10.4MB)
# 테스트 19 〉	통과 (5.64ms, 10.4MB)
# 테스트 20 〉	통과 (9.71ms, 10.2MB)
# 테스트 21 〉	통과 (51.55ms, 10.2MB)
# 테스트 22 〉	통과 (48.82ms, 10.4MB)
# 테스트 23 〉	통과 (12.42ms, 10.2MB)
# 테스트 24 〉	통과 (52.86ms, 10.3MB)
# 테스트 25 〉	통과 (0.07ms, 10.1MB)
# 테스트 26 〉	통과 (0.72ms, 10.2MB)
# 효율성  테스트
# 테스트 1 〉	실패 (시간 초과)
# 테스트 2 〉	실패 (시간 초과)
# 테스트 3 〉	실패 (시간 초과)
# 테스트 4 〉	실패 (시간 초과)
# 테스트 5 〉	실패 (시간 초과)
# 테스트 6 〉	실패 (시간 초과)
# 테스트 7 〉	실패 (시간 초과)
# 채점 결과
# 정확성: 78.8
# 효율성: 0.0
# 합계: 78.8 / 100.0


# keys를 list로 만들지 않은 버전 
def solution(k, room_number):
    #k=방의개수
    #room_number=원하는 방번호 
    answer = []
    reserve = dict()
    for room in room_number:
        if room in reserve:
            not_empty=reserve.keys()
            next = reserve[room]
            while True:
                if next not in not_empty:
                    answer.append(next)
                    reserve[next] = next + 1
                    break
                else:
                    next += 1
            
        else: 
            answer.append(room)
            reserve[room] = room + 1
    
    return answer

# 정확성  테스트
# 테스트 1 〉	통과 (0.00ms, 10.2MB)
# 테스트 2 〉	통과 (0.01ms, 10.2MB)
# 테스트 3 〉	통과 (0.01ms, 10.2MB)
# 테스트 4 〉	통과 (0.20ms, 10.3MB)
# 테스트 5 〉	통과 (0.01ms, 10.2MB)
# 테스트 6 〉	통과 (0.02ms, 10.1MB)
# 테스트 7 〉	통과 (0.02ms, 10.2MB)
# 테스트 8 〉	통과 (0.01ms, 10.2MB)
# 테스트 9 〉	통과 (0.01ms, 10.2MB)
# 테스트 10 〉	통과 (0.01ms, 10.2MB)
# 테스트 11 〉	통과 (0.01ms, 10.2MB)
# 테스트 12 〉	통과 (0.01ms, 10.1MB)
# 테스트 13 〉	통과 (0.01ms, 10.2MB)
# 테스트 14 〉	통과 (0.01ms, 10.3MB)
# 테스트 15 〉	통과 (0.04ms, 10.1MB)
# 테스트 16 〉	통과 (0.05ms, 10MB)
# 테스트 17 〉	통과 (0.06ms, 10.2MB)
# 테스트 18 〉	통과 (0.17ms, 10.2MB)
# 테스트 19 〉	통과 (0.38ms, 10.3MB)
# 테스트 20 〉	통과 (0.50ms, 10.2MB)
# 테스트 21 〉	통과 (1.47ms, 10.3MB)
# 테스트 22 〉	통과 (1.56ms, 10.3MB)
# 테스트 23 〉	통과 (0.55ms, 10.4MB)
# 테스트 24 〉	통과 (1.32ms, 10.3MB)
# 테스트 25 〉	통과 (0.02ms, 10.2MB)
# 테스트 26 〉	통과 (0.10ms, 10.2MB)
# 효율성  테스트
# 테스트 1 〉	실패 (시간 초과)
# 테스트 2 〉	실패 (시간 초과)
# 테스트 3 〉	실패 (시간 초과)
# 테스트 4 〉	실패 (시간 초과)
# 테스트 5 〉	실패 (시간 초과)
# 테스트 6 〉	실패 (시간 초과)
# 테스트 7 〉	실패 (시간 초과)
# 채점 결과
# 정확성: 78.8
# 효율성: 0.0
# 합계: 78.8 / 100.0

def solution(k, room_number):
    #k=방의개수
    #room_number=원하는 방번호 
    answer = []
    reserve = dict()
    
    for room in room_number:
        if room in reserve:
            not_empty=reserve.keys()
            next = reserve[room]
            while next in not_empty:
                next = reserve[next]
            answer.append(next)
            reserve[next] = next + 1
            
        else: 
            answer.append(room)
            reserve[room] = room + 1
    
    return answer

# 정확성  테스트
# 테스트 1 〉	통과 (0.00ms, 10.3MB)
# 테스트 2 〉	통과 (0.01ms, 10.2MB)
# 테스트 3 〉	통과 (0.01ms, 10.2MB)
# 테스트 4 〉	통과 (0.23ms, 10.2MB)
# 테스트 5 〉	통과 (0.01ms, 10.2MB)
# 테스트 6 〉	통과 (0.02ms, 10.2MB)
# 테스트 7 〉	통과 (0.02ms, 10.2MB)
# 테스트 8 〉	통과 (0.01ms, 10.2MB)
# 테스트 9 〉	통과 (0.01ms, 10.1MB)
# 테스트 10 〉	통과 (0.01ms, 10.2MB)
# 테스트 11 〉	통과 (0.01ms, 10.2MB)
# 테스트 12 〉	통과 (0.02ms, 10.1MB)
# 테스트 13 〉	통과 (0.01ms, 10.2MB)
# 테스트 14 〉	통과 (0.01ms, 10.2MB)
# 테스트 15 〉	통과 (0.04ms, 10.2MB)
# 테스트 16 〉	통과 (0.05ms, 10.2MB)
# 테스트 17 〉	통과 (0.06ms, 10.1MB)
# 테스트 18 〉	통과 (0.16ms, 10.1MB)
# 테스트 19 〉	통과 (0.37ms, 10MB)
# 테스트 20 〉	통과 (0.43ms, 10.3MB)
# 테스트 21 〉	통과 (1.15ms, 10.3MB)
# 테스트 22 〉	통과 (1.08ms, 10.4MB)
# 테스트 23 〉	통과 (0.51ms, 10.3MB)
# 테스트 24 〉	통과 (1.10ms, 10.4MB)
# 테스트 25 〉	통과 (0.03ms, 10.2MB)
# 테스트 26 〉	통과 (0.11ms, 10.2MB)
# 효율성  테스트
# 테스트 1 〉	실패 (시간 초과)
# 테스트 2 〉	실패 (시간 초과)
# 테스트 3 〉	실패 (시간 초과)
# 테스트 4 〉	실패 (시간 초과)
# 테스트 5 〉	실패 (시간 초과)
# 테스트 6 〉	실패 (시간 초과)
# 테스트 7 〉	실패 (시간 초과)
# 채점 결과
# 정확성: 78.8
# 효율성: 0.0
# 합계: 78.8 / 100.0




def solution(k, room_number):
    #k=방의개수
    #room_number=원하는 방번호 
    answer = []
    reserve = dict()
    
    for room in room_number:
        if room in reserve:
            arr=[room]
            next = reserve[room]
            while next in reserve:
                arr.append(next)
                next = reserve[next]
            # 방 예약하기 
            answer.append(next)
            reserve[next] = next + 1
            
            for each in arr:
                reserve[each] = next + 1
            
        else: 
            answer.append(room)
            reserve[room] = room + 1
    
    return answer

# 정확성  테스트
# 테스트 1 〉	통과 (0.00ms, 10.2MB)
# 테스트 2 〉	통과 (0.01ms, 10.2MB)
# 테스트 3 〉	통과 (0.01ms, 10.3MB)
# 테스트 4 〉	통과 (0.08ms, 10.2MB)
# 테스트 5 〉	통과 (0.01ms, 10.2MB)
# 테스트 6 〉	통과 (0.02ms, 10.2MB)
# 테스트 7 〉	통과 (0.02ms, 10.2MB)
# 테스트 8 〉	통과 (0.01ms, 10.2MB)
# 테스트 9 〉	통과 (0.01ms, 10.2MB)
# 테스트 10 〉	통과 (0.01ms, 10.1MB)
# 테스트 11 〉	통과 (0.01ms, 10.1MB)
# 테스트 12 〉	통과 (0.02ms, 10.2MB)
# 테스트 13 〉	통과 (0.01ms, 10.2MB)
# 테스트 14 〉	통과 (0.01ms, 10.1MB)
# 테스트 15 〉	통과 (0.05ms, 10.2MB)
# 테스트 16 〉	통과 (0.06ms, 10.2MB)
# 테스트 17 〉	통과 (0.07ms, 10.2MB)
# 테스트 18 〉	통과 (0.12ms, 10.2MB)
# 테스트 19 〉	통과 (0.34ms, 10.2MB)
# 테스트 20 〉	통과 (0.42ms, 10.3MB)
# 테스트 21 〉	통과 (0.89ms, 10.3MB)
# 테스트 22 〉	통과 (0.90ms, 10.3MB)
# 테스트 23 〉	통과 (0.62ms, 10.3MB)
# 테스트 24 〉	통과 (0.99ms, 10.2MB)
# 테스트 25 〉	통과 (0.02ms, 10.1MB)
# 테스트 26 〉	통과 (0.05ms, 10.1MB)
# 효율성  테스트
# 테스트 1 〉	통과 (414.00ms, 53.4MB)
# 테스트 2 〉	통과 (473.75ms, 53.4MB)
# 테스트 3 〉	통과 (409.89ms, 53.4MB)
# 테스트 4 〉	통과 (345.13ms, 53.3MB)
# 테스트 5 〉	통과 (138.84ms, 54.2MB)
# 테스트 6 〉	통과 (453.22ms, 54.6MB)
# 테스트 7 〉	통과 (467.55ms, 61.2MB)