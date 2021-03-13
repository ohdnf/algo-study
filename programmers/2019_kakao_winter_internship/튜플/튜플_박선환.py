def solution(s):
    s = s[1:-1].split('}')
    basket = []
    for i in range(len(s) - 1):
        element = s[i].strip(',').strip('{').split(',')
        basket.append(set(map(int, element)))
    basket.sort(key=lambda x: len(x))
    answer = [list(basket[0])[0]]
    for i in range(len(basket) - 1):
        answer.append(list(basket[i+1] - basket[i])[0])
    return answer

'''
테스트 1 〉	통과 (0.04ms, 10.3MB)
테스트 2 〉	통과 (0.03ms, 10.4MB)
테스트 3 〉	통과 (0.03ms, 10.3MB)
테스트 4 〉	통과 (0.07ms, 10.3MB)
테스트 5 〉	통과 (0.28ms, 10.4MB)
테스트 6 〉	통과 (0.58ms, 10.4MB)
테스트 7 〉	통과 (5.51ms, 12.1MB)
테스트 8 〉	통과 (13.82ms, 15.9MB)
테스트 9 〉	통과 (7.47ms, 12.8MB)
테스트 10 〉	통과 (16.13ms, 16.4MB)
테스트 11 〉	통과 (20.92ms, 19.1MB)
테스트 12 〉	통과 (31.39ms, 23.4MB)
테스트 13 〉	통과 (34.01ms, 23.3MB)
테스트 14 〉	통과 (34.20ms, 23.5MB)
테스트 15 〉	통과 (0.03ms, 10.3MB)
'''