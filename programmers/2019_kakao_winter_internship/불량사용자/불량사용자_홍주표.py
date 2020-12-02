import re

def solution(user_id, banned_id):
    # 정규표현식을 사용해 제재 아이디가 될 수 있는 사용자 목록 만들기
    id_list = []
    for banned in banned_id:
        banned = r'\b' + banned.replace('*', '.') + r'\b'
        matched_users = []
        for user in user_id:
            matched = re.match(banned, user)
            # print(matched)
            if matched:
                matched_users.append(matched.group())
        # print(banned, matched_ids)
        id_list.append(matched_users)
    # print(id_list)

    # 모든 경우의 수 계산
    def dfs(index, last, blacklist):
        if index == last:
            if len(banned_id) == len(blacklist):
                # print(blacklist)
                answer.add(frozenset(blacklist[:]))
        else:
            for matched_id in id_list[index]:
                if matched_id in blacklist:
                    continue
                blacklist.append(matched_id)
                dfs(index + 1, last, blacklist)
                blacklist.pop()

    answer = set()
    dfs(0, len(id_list), [])
    # print(answer)
    return len(answer)


if __name__ == '__main__':
    print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],
                   ["fr*d*", "abc1**"]), 2)
    print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],
                   ["*rodo", "*rodo", "******"]), 2)
    print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],
                   ["fr*d*", "*rodo", "******", "******"]), 3)

"""
테스트 1 〉	통과 (0.09ms, 10.2MB)
테스트 2 〉	통과 (0.28ms, 10.2MB)
테스트 3 〉	통과 (0.22ms, 10.2MB)
테스트 4 〉	통과 (0.27ms, 10.2MB)
테스트 5 〉	통과 (79.74ms, 10.3MB)
테스트 6 〉	통과 (1.20ms, 10.2MB)
테스트 7 〉	통과 (0.26ms, 10.2MB)
테스트 8 〉	통과 (0.33ms, 10.3MB)
테스트 9 〉	통과 (0.30ms, 10.3MB)
테스트 10 〉	통과 (0.49ms, 10.2MB)
테스트 11 〉	통과 (0.38ms, 10.2MB)
"""
