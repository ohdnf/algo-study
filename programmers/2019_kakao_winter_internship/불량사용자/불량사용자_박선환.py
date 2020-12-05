# 첫 번째 방법
import re

def solution(user_id, banned_id):
    answers = set()
    picked = [0] * len(user_id)
    def dfs(i, temp):
        if i == len(banned_id):
            if len(temp) == i:
                temp = tuple(sorted(temp))
                answers.add(temp)
            return
        c_ban_id = banned_id[i]
        p = re.compile(c_ban_id.replace('*', '.'))
        for j in range(len(user_id)):
            if not picked[j]:
                c_user_id = user_id[j]
                if len(c_user_id) == len(c_ban_id) and p.match(c_user_id):
                    picked[j] = 1
                    dfs(i+1, temp + [c_user_id])
                    picked[j] = 0
    dfs(0, [])
    return len(answers)
'''
정확성 테스트
테스트 1 〉	통과 (0.07ms, 10.3MB)
테스트 2 〉	통과 (0.26ms, 10.2MB)
테스트 3 〉	통과 (0.22ms, 10.2MB)
테스트 4 〉	통과 (0.22ms, 10.3MB)
테스트 5 〉	통과 (140.82ms, 10.3MB)
테스트 6 〉	통과 (2.28ms, 10.3MB)
테스트 7 〉	통과 (0.25ms, 10.3MB)
테스트 8 〉	통과 (0.28ms, 10.2MB)
테스트 9 〉	통과 (0.30ms, 10.3MB)
테스트 10 〉	통과 (0.36ms, 10.2MB)
테스트 11 〉	통과 (0.36ms, 10.3MB)
'''

# ---------------------------------------
# 두 번째 방법
import re

def solution(user_id, banned_id):
    candidates = []
    for c_banned_id in banned_id:
        temp = []
        for i in range(len(user_id)):
            c_user_id = user_id[i]
            p = re.compile(c_banned_id.replace('*', '.'))
            if len(c_user_id) == len(c_banned_id) and p.match(c_user_id):
                temp.append(i)
        if len(temp):
            candidates.append(temp)
    
    if len(candidates) != len(banned_id):
        return 0
    else:
        answers = set()
        picked = [0] * len(user_id)
        def dfs(i, temp):
            if i == len(banned_id):
                if len(temp) == i:
                    temp = tuple(sorted(temp))
                    answers.add(temp)
                return
            for n in candidates[i]:
                if not picked[n]:
                    picked[n] = 1
                    dfs(i+1, temp + [n])
                    picked[n] = 0
        dfs(0, [])
        return len(answers)
'''
정확성 테스트
테스트 1 〉	통과 (0.08ms, 10.2MB)
테스트 2 〉	통과 (0.24ms, 10.3MB)
테스트 3 〉	통과 (0.92ms, 10.3MB)
테스트 4 〉	통과 (0.22ms, 10.3MB)
테스트 5 〉	통과 (67.08ms, 10.2MB)
테스트 6 〉	통과 (1.08ms, 10.3MB)
테스트 7 〉	통과 (0.24ms, 10.3MB)
테스트 8 〉	통과 (0.28ms, 10.3MB)
테스트 9 〉	통과 (0.26ms, 10.3MB)
테스트 10 〉	통과 (0.43ms, 10.2MB)
테스트 11 〉	통과 (0.32ms, 10.3MB)
'''