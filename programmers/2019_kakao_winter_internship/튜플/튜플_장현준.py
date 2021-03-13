def solution(s):
    answer = []
    used = dict()
    for lst in sorted(map(lambda x: tuple(map(int, x.split(','))), s[2:-2].split('},{')), key=lambda x: len(x)):
        for num in lst:
            if num not in used:
                used[num] = 1
                answer.append(num)
                break
    return answer
# 테스트 1 〉	통과 (0.04ms, 10.2MB)
# 테스트 2 〉	통과 (0.03ms, 10.3MB)
# 테스트 3 〉	통과 (0.03ms, 10.3MB)
# 테스트 4 〉	통과 (0.06ms, 10.4MB)
# 테스트 5 〉	통과 (0.24ms, 10.4MB)
# 테스트 6 〉	통과 (0.46ms, 10.3MB)
# 테스트 7 〉	통과 (3.81ms, 11.1MB)
# 테스트 8 〉	통과 (13.00ms, 12.7MB)
# 테스트 9 〉	통과 (5.89ms, 11.6MB)
# 테스트 10 〉	통과 (12.25ms, 12.8MB)
# 테스트 11 〉	통과 (16.52ms, 14.2MB)
# 테스트 12 〉	통과 (21.77ms, 16.4MB)
# 테스트 13 〉	통과 (20.88ms, 16.4MB)
# 테스트 14 〉	통과 (21.97ms, 16.5MB)
# 테스트 15 〉	통과 (0.03ms, 10.3MB)