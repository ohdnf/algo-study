from collections import Counter

def solution(s):
    answer = []
    s1 = s[2:-2].split('},{')
    s1.sort(key=len)
    for s2 in s1:
        s3 = list(map(int, s2.split(',')))
        answer.extend(list(Counter(s3) - Counter(answer)))
    return answer


"""
테스트 1 〉	통과 (0.10ms, 10.2MB)
테스트 2 〉	통과 (0.08ms, 10.4MB)
테스트 3 〉	통과 (0.06ms, 10.3MB)
테스트 4 〉	통과 (0.19ms, 10.3MB)
테스트 5 〉	통과 (0.73ms, 10.3MB)
테스트 6 〉	통과 (1.41ms, 10.3MB)
테스트 7 〉	통과 (10.09ms, 10.4MB)
테스트 8 〉	통과 (28.32ms, 11.1MB)
테스트 9 〉	통과 (13.93ms, 10.6MB)
테스트 10 〉	통과 (30.37ms, 11.1MB)
테스트 11 〉	통과 (39.42ms, 11.4MB)
테스트 12 〉	통과 (53.78ms, 12.4MB)
테스트 13 〉	통과 (53.32ms, 12.5MB)
테스트 14 〉	통과 (54.69ms, 12.3MB)
테스트 15 〉	통과 (0.06ms, 10.4MB)
"""
