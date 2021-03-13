from collections import OrderedDict 
def solution(s):
    longest_tuple = []
    
    s = s[2:len(s)-2]
    s = s.replace("},{", "/")
    s = s.split("/")

    dict = OrderedDict()
    for i in s:
        arr = tuple(map(int, i.split(',')))
        for i in arr:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1

    sorted_dict = sorted(dict.items(), key = lambda x: x[1], reverse=True)

    for i in sorted_dict:
        longest_tuple.append(i[0])

    return longest_tuple

'''
테스트 1 〉	통과 (0.05ms, 10.4MB)
테스트 2 〉	통과 (0.03ms, 10.3MB)
테스트 3 〉	통과 (0.03ms, 10.3MB)
테스트 4 〉	통과 (0.08ms, 10.3MB)
테스트 5 〉	통과 (0.33ms, 10.3MB)
테스트 6 〉	통과 (0.70ms, 10.3MB)
테스트 7 〉	통과 (6.44ms, 10.6MB)
테스트 8 〉	통과 (17.20ms, 11MB)
테스트 9 〉	통과 (9.17ms, 10.5MB)
테스트 10 〉	통과 (19.19ms, 10.8MB)
테스트 11 〉	통과 (26.05ms, 11.4MB)
테스트 12 〉	통과 (35.50ms, 12.1MB)
테스트 13 〉	통과 (36.24ms, 12.4MB)
테스트 14 〉	통과 (36.11ms, 12.4MB)
테스트 15 〉	통과 (0.04ms, 10.3MB)
'''