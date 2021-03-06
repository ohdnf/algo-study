def solution(words):
    # trie 구조 만들기
    trie = {}
    for word in words:
        curr = trie
        for idx in range(len(word)-1):
            char = word[idx]
            if char not in curr:
                curr[char] = { 'cnt': 0, 'end': 0 }
            curr = curr[char]
            curr['cnt'] += 1
        # 마지막 문자 처리
        char = word[-1]
        if char not in curr:
            curr[char] = { 'cnt': 0, 'end': 0 }
        curr = curr[char]
        curr['cnt'] += 1
        curr['end'] += 1
    # print(trie)
    # 단어 검색
    # 검색 종료되는 조건은
    # 1. 단어의 모든 문자를 입력했을 때
    # 2. trie 구조에서 현재 문자 기준으로 branch가 하나일 때
    answer = 0
    for word in words:
        curr = trie
        input_cnt = 0
        for char in word:
            curr = curr[char]
            input_cnt += 1
            if curr['cnt'] == 1:
                break
        answer += input_cnt
        # print(word, input_cnt)
    return answer

"""
테스트 1 〉	통과 (0.01ms, 10.1MB)
테스트 2 〉	통과 (0.02ms, 10.2MB)
테스트 3 〉	통과 (0.02ms, 10.1MB)
테스트 4 〉	통과 (0.02ms, 10.2MB)
테스트 5 〉	통과 (0.02ms, 10.1MB)
테스트 6 〉	통과 (815.23ms, 184MB)
테스트 7 〉	통과 (0.02ms, 10.1MB)
테스트 8 〉	통과 (862.80ms, 184MB)
테스트 9 〉	통과 (0.02ms, 10.1MB)
테스트 10 〉	통과 (0.02ms, 10.2MB)
테스트 11 〉	통과 (0.02ms, 10.1MB)
테스트 12 〉	통과 (852.25ms, 183MB)
테스트 13 〉	통과 (798.06ms, 184MB)
테스트 14 〉	통과 (779.87ms, 243MB)
테스트 15 〉	통과 (0.02ms, 10.2MB)
테스트 16 〉	통과 (837.63ms, 184MB)
테스트 17 〉	통과 (909.29ms, 183MB)
테스트 18 〉	통과 (0.03ms, 10.2MB)
테스트 19 〉	통과 (784.05ms, 243MB)
테스트 20 〉	통과 (819.29ms, 184MB)
테스트 21 〉	통과 (742.12ms, 243MB)
테스트 22 〉	통과 (749.44ms, 243MB)
"""
