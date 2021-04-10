'''카카오블라인드19 오픈채팅방
출력
- "[닉네임]님이 들어왔습니다."
- "[닉네임]님이 나갔습니다."

닉네임 변경
- 나갔다 들어오기
- 안에서 변경하기

닉네임 변경시
- 채팅방의 메시지 닉네임 모두 변화

최종 출력 메시지

입력
- record
    - 길이 1 ~ 100,000
    - 행동 유저아이디 (닉네임)
        - Enter 유저아이디 닉네임
        - Leave 유저아이디
        - Change 유저아이디 닉네임
'''
from collections import defaultdict
def solution(records):
    id2nickname = defaultdict()
    act2string = {
        'Enter': '님이 들어왔습니다.',
        "Leave": '님이 나갔습니다.',
    }
    result = []
    for record in records:
        temp = record.split()
        if temp[0] == 'Enter':
            result.append(('Enter', temp[1]))
            id2nickname[temp[1]] = temp[2]
        elif temp[0] == 'Leave':
            result.append(('Leave', temp[1]))
        elif temp[0] == 'Change':
            id2nickname[temp[1]] = temp[2]
    result = [id2nickname[uid]+act2string[act] for act, uid in result]
    
    return result
'''
정확성  테스트
테스트 1 〉	통과 (0.02ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.3MB)
테스트 3 〉	통과 (0.04ms, 10.2MB)
테스트 4 〉	통과 (0.04ms, 10.2MB)
테스트 5 〉	통과 (0.85ms, 10.5MB)
테스트 6 〉	통과 (0.82ms, 10.6MB)
테스트 7 〉	통과 (0.72ms, 10.4MB)
테스트 8 〉	통과 (0.77ms, 10.6MB)
테스트 9 〉	통과 (0.90ms, 10.7MB)
테스트 10 〉통과 (0.90ms, 10.4MB)
테스트 11 〉통과 (0.60ms, 10.3MB)
테스트 12 〉통과 (0.46ms, 10.4MB)
테스트 13 〉통과 (0.82ms, 10.5MB)
테스트 14 〉통과 (0.88ms, 10.7MB)
테스트 15 〉통과 (0.02ms, 10.3MB)
테스트 16 〉통과 (0.02ms, 10.2MB)
테스트 17 〉통과 (0.09ms, 10.2MB)
테스트 18 〉통과 (0.09ms, 10.2MB)
테스트 19 〉통과 (0.82ms, 10.6MB)
테스트 20 〉통과 (0.69ms, 10.4MB)
테스트 21 〉통과 (0.77ms, 10.3MB)
테스트 22 〉통과 (0.77ms, 10.4MB)
테스트 23 〉통과 (0.81ms, 10.7MB)
테스트 24 〉통과 (0.95ms, 10.7MB)
테스트 25 〉통과 (72.71ms, 54.2MB)
테스트 26 〉통과 (80.40ms, 61.9MB)
테스트 27 〉통과 (79.80ms, 63.4MB)
테스트 28 〉통과 (91.56ms, 66.3MB)
테스트 29 〉통과 (89.51ms, 66.4MB)
테스트 30 〉통과 (57.73ms, 49.4MB)
테스트 31 〉통과 (62.54ms, 57MB)
테스트 32 〉통과 (54.87ms, 52.8MB)
'''