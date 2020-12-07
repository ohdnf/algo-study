def solution(user_id, banned_id):
    answer = dict()
    uids = [0] * len(user_id)
    bids = [0] * len(banned_id)
    # bid에 uid가 해당하는지 T/F 리턴한다.
    def check(bid, uid):
        if len(bid) != len(uid): return False
        for i in range(len(bid)):
            if bid[i] == "*" or bid[i] == uid[i]: continue
            return False
        return True
    # banned_id[n] 과 uids를 비교한다.
    def dfs(n, uids):
        # 3. 마지막에 생성된 제재 목록을 넣는다.
        if n == len(banned_id):
            uids_key = ''.join(map(str,uids))
            if uids_key not in answer: answer[uids_key] = 1
            return                
        for j in range(len(uids)):
            if uids[j]: continue
            # 1. 각 유저아이디가 banned_id[n]에 해당하는지 체크한다.
            if check(banned_id[n], user_id[j]):
                # 2. 해당하면, 제재 목록에 넣고, 다음을 진행한다.
                uids[j] = 1
                dfs(n+1, uids)
                uids[j] = 0
    dfs(0, uids)
    return len(answer)

'''
테스트 1 〉	통과 (0.02ms, 10.2MB)
테스트 2 〉	통과 (0.11ms, 10.4MB)
테스트 3 〉	통과 (0.10ms, 10.3MB)
테스트 4 〉	통과 (0.06ms, 10.3MB)
테스트 5 〉	통과 (163.86ms, 10.3MB)
테스트 6 〉	통과 (2.59ms, 10.3MB)
테스트 7 〉	통과 (0.08ms, 10.3MB)
테스트 8 〉	통과 (0.09ms, 10.3MB)
테스트 9 〉	통과 (0.13ms, 10.3MB)
테스트 10 〉통과 (0.04ms, 10.3MB)
테스트 11 〉통과 (0.13ms, 10.3MB)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
'''

# 아래는 예전에 풀어본 로직

answer = []

# dfs(단계 k, 각 user_id 선택여부 ulst, 사용한 banned_id blst, 참조위한 user_id, banned_id)
def dfs(k, ulst, blst, user_id, banned_id):
    # print(ulst, blst)
    # 4. 중복 X => answer.append
    if k == len(user_id):
        if len(ulst) == len(banned_id) and ulst not in answer:
            answer.append(ulst)
        return

    uid = user_id[k]
    # 3-1. 순회 기준 2 banned_id => 해당하는 것이 있다면 선택
    for idx, bid in enumerate(banned_id):
        if len(bid) != len(uid) or idx in blst:
            continue
        for i, st in enumerate(bid):
            if st == "*" or st == uid[i]:
                continue
            break
        else:
            # 해당되는 것이 있다면 선택
            dfs(k+1, ulst+[k], blst+[idx], user_id, banned_id)
    # 3-2. default : 미선택
    dfs(k+1, ulst, blst, user_id, banned_id)

def solution(user_id, banned_id):
    global answer
    # 4:49
    # 1. dict 형식으로 => 길이 : [해당 길이 id들] 모집
#     users = dict()
#     for uid in user_id:
#         if len(uid) in users:
#             users[len(uid)].append(uid)
#         else:
#             users[len(uid)] = [ uid ]
#     bans = dict()
    
#     for bid in banned_id:
#         if len(bid) in bans:
#             bans[len(bid)].append(bid)
#         else:
#             bans[len(bid)] = [ bid ]
            
    # 메인 로직
    dfs(0, [], [], user_id, banned_id)
    
    return len(answer)

'''
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.32ms, 10.2MB)
테스트 3 〉	통과 (0.15ms, 10.2MB)
테스트 4 〉	통과 (0.12ms, 10.3MB)
테스트 5 〉	통과 (1838.78ms, 10.3MB)
테스트 6 〉	통과 (10.68ms, 10.2MB)
테스트 7 〉	통과 (0.22ms, 10.2MB)
테스트 8 〉	통과 (0.99ms, 10.3MB)
테스트 9 〉	통과 (0.38ms, 10.3MB)
테스트 10 〉	통과 (0.87ms, 10.2MB)
테스트 11 〉	통과 (0.64ms, 10.3MB)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
'''

