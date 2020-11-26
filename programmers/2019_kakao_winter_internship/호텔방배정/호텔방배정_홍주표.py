def solution1(k, room_number):
    answer = []

    booked = dict()

    for room in room_number:
        if room in booked:
            next_room = booked[room]
            while next_room in booked:
                next_room = booked[next_room]
            for checked in range(room, next_room + 1):
                booked[checked] = next_room + 1
            answer.append(next_room)
        else:
            booked[room] = room + 1
            answer.append(room)

    return answer

"""
정확성 테스트
테스트 1 〉	통과 (0.00ms, 10.1MB)
테스트 2 〉	통과 (0.01ms, 10.1MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.21ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.02ms, 10.1MB)
테스트 7 〉	통과 (0.02ms, 10.2MB)
테스트 8 〉	통과 (0.01ms, 10.3MB)
테스트 9 〉	통과 (0.01ms, 10.2MB)
테스트 10 〉	통과 (0.01ms, 10.1MB)
테스트 11 〉	통과 (0.01ms, 10MB)
테스트 12 〉	통과 (0.01ms, 10.2MB)
테스트 13 〉	통과 (0.01ms, 10.2MB)
테스트 14 〉	통과 (0.01ms, 10.2MB)
테스트 15 〉	통과 (0.03ms, 10.2MB)
테스트 16 〉	통과 (0.05ms, 10.2MB)
테스트 17 〉	통과 (0.05ms, 10.2MB)
테스트 18 〉	통과 (0.13ms, 10.2MB)
테스트 19 〉	통과 (0.32ms, 10.2MB)
테스트 20 〉	통과 (0.41ms, 10.2MB)
테스트 21 〉	통과 (1.20ms, 10.3MB)
테스트 22 〉	통과 (1.09ms, 10.2MB)
테스트 23 〉	통과 (0.47ms, 10.3MB)
테스트 24 〉	통과 (1.59ms, 10.3MB)
테스트 25 〉	통과 (0.02ms, 10.2MB)
테스트 26 〉	통과 (0.11ms, 10.2MB)

효율성 테스트
테스트 1 〉	실패 (시간 초과)
테스트 2 〉	실패 (시간 초과)
테스트 3 〉	실패 (시간 초과)
테스트 4 〉	실패 (시간 초과)
테스트 5 〉	실패 (시간 초과)
테스트 6 〉	실패 (시간 초과)
테스트 7 〉	실패 (시간 초과)

채점 결과
정확성: 78.8
효율성: 0.0
합계: 78.8 / 100.0
"""


def solution(k, room_number):
    answer = []

    booked = dict()     # 예약된 방일 경우 배정받을 다음 방 번호를 가리키는 딕셔너리

    for room in room_number:
        if room in booked:
            checked = [room]            # 예약된 방을 업데이트하기 위한 배열
            next_room = booked[room]    # 다음 방 탐색
            while next_room in booked:
                checked.append(next_room)
                next_room = booked[next_room]
            # 빈 방 배정
            answer.append(next_room)
            # 탐색한 모든 방의 다음 방 번호를 업데이트
            booked[next_room] = next_room + 1
            for checked_room in checked:
                booked[checked_room] = next_room + 1

        else:
            booked[room] = room + 1
            answer.append(room)

    return answer


"""
정확성 테스트
테스트 1 〉	통과 (0.00ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.09ms, 10.3MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.02ms, 10.2MB)
테스트 7 〉	통과 (0.02ms, 10.2MB)
테스트 8 〉	통과 (0.01ms, 10.1MB)
테스트 9 〉	통과 (0.01ms, 10.2MB)
테스트 10 〉	통과 (0.01ms, 10.3MB)
테스트 11 〉	통과 (0.01ms, 10.2MB)
테스트 12 〉	통과 (0.02ms, 10.2MB)
테스트 13 〉	통과 (0.01ms, 10.2MB)
테스트 14 〉	통과 (0.01ms, 10.1MB)
테스트 15 〉	통과 (0.04ms, 10.2MB)
테스트 16 〉	통과 (0.06ms, 10.2MB)
테스트 17 〉	통과 (0.07ms, 10.2MB)
테스트 18 〉	통과 (0.17ms, 10.2MB)
테스트 19 〉	통과 (0.39ms, 10.3MB)
테스트 20 〉	통과 (0.44ms, 10.3MB)
테스트 21 〉	통과 (0.85ms, 10.3MB)
테스트 22 〉	통과 (0.88ms, 10.4MB)
테스트 23 〉	통과 (0.57ms, 10.3MB)
테스트 24 〉	통과 (0.96ms, 10.3MB)
테스트 25 〉	통과 (0.02ms, 10.2MB)
테스트 26 〉	통과 (0.03ms, 10.2MB)

효율성  테스트
테스트 1 〉	통과 (405.78ms, 53.4MB)
테스트 2 〉	통과 (403.09ms, 53.4MB)
테스트 3 〉	통과 (416.27ms, 53.4MB)
테스트 4 〉	통과 (334.32ms, 53.2MB)
테스트 5 〉	통과 (137.12ms, 54.2MB)
테스트 6 〉	통과 (436.15ms, 54.7MB)
테스트 7 〉	통과 (458.28ms, 61.3MB)
"""