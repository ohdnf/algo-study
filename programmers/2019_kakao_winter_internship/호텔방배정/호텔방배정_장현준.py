def solution(k, room_number):
    answer = []
    nextRoom = dict()
    for number in room_number:
        # 현재 number번 방부터 시작하여 서치 시작
        # 서치 경로
        records = []
        while True:
            # 서치 경로 기록
            records.append(number)
            # 1. 빈방인가요? => 빈방이면 == nextRoom[number]:값 으로 하는 key : value 쌍이 없다
            if number not in nextRoom:
                # 2-1. 빈방이면 끝 => 배정된 방 번호는 number
                answer.append(number)
                break
            # 2-2. 아니면 계속 
            number = nextRoom[number]
        # 3. 빈방을 찾은 후, 그동안 들렀던 방의 부모+1 수행
        for n in records:
            nextRoom[n] = number + 1
    # 결과 출력
    return answer

# 로직 정리
# 손님이 원하는 number번 방부터 시작하여 빈방인지 확인한다.
# 빈방이 아니면, nextRoom[number]번 방이 빈방인지 확인한다. (number 업데이트) 
# 해당 number에서 빈방을 찾으면 => 리턴된 빈방은 배정되고(answer), 지금까지 확인했던 방들의 nextRomm값을 갱신한다.
'''
정확성  테스트
테스트 1 〉	통과 (0.00ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.09ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.02ms, 10.2MB)
테스트 7 〉	통과 (0.02ms, 10.1MB)
테스트 8 〉	통과 (0.01ms, 10.2MB)
테스트 9 〉	통과 (0.01ms, 10.2MB)
테스트 10 〉	통과 (0.01ms, 10.2MB)
테스트 11 〉	통과 (0.01ms, 10.1MB)
테스트 12 〉	통과 (0.02ms, 10.1MB)
테스트 13 〉	통과 (0.01ms, 10.2MB)
테스트 14 〉	통과 (0.02ms, 10.2MB)
테스트 15 〉	통과 (0.06ms, 10.2MB)
테스트 16 〉	통과 (0.07ms, 10.2MB)
테스트 17 〉	통과 (0.08ms, 10.2MB)
테스트 18 〉	통과 (0.19ms, 10.2MB)
테스트 19 〉	통과 (0.96ms, 10.2MB)
테스트 20 〉	통과 (0.50ms, 10.3MB)
테스트 21 〉	통과 (0.91ms, 10.3MB)
테스트 22 〉	통과 (0.96ms, 10.3MB)
테스트 23 〉	통과 (0.72ms, 10.4MB)
테스트 24 〉	통과 (1.04ms, 10.4MB)
테스트 25 〉	통과 (0.03ms, 10.2MB)
테스트 26 〉	통과 (0.06ms, 10.3MB)
효율성  테스트
테스트 1 〉	통과 (408.13ms, 53.5MB)
테스트 2 〉	통과 (454.29ms, 53.4MB)
테스트 3 〉	통과 (428.38ms, 53.4MB)
테스트 4 〉	통과 (351.54ms, 53MB)
테스트 5 〉	통과 (164.93ms, 54.2MB)
테스트 6 〉	통과 (432.90ms, 54.6MB)
테스트 7 〉	통과 (469.47ms, 61.4MB)
채점 결과
정확성: 78.8
효율성: 21.2
합계: 100.0 / 100.0
'''