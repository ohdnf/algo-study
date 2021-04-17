def solution(orders, course):
    from collections import defaultdict
    from itertools import combinations
    
    for i in range(len(orders)):
        orders[i] = sorted(orders[i])

    answer = []
    dict = defaultdict()
    course_num_dict = defaultdict()
    
    for order in orders:
        for num in course:
            combis = list(combinations(list(order), num))
            if combis:
                for combi in combis:
                    try:
                        dict[''.join(combi)] += 1
                    except:
                        dict[''.join(combi)] = 1

    for combi in dict:
        try:
            if course_num_dict[len(combi)] < dict[combi]:
                course_num_dict[len(combi)] = dict[combi]
        except:
            course_num_dict[len(combi)] = dict[combi]
        
    for combi in dict:
        if course_num_dict[len(combi)] >= 2 and dict[combi] == course_num_dict[len(combi)]:
            answer.append(combi)
    return sorted(answer)

'''
테스트 1 〉	통과 (0.19ms, 10.3MB)
테스트 2 〉	통과 (0.12ms, 10.2MB)
테스트 3 〉	통과 (0.16ms, 10.2MB)
테스트 4 〉	통과 (0.19ms, 10.2MB)
테스트 5 〉	통과 (0.17ms, 10.4MB)
테스트 6 〉	통과 (0.47ms, 10.3MB)
테스트 7 〉	통과 (0.44ms, 10.2MB)
테스트 8 〉	통과 (2.62ms, 10.2MB)
테스트 9 〉	통과 (1.91ms, 10.3MB)
테스트 10 〉	통과 (3.84ms, 10.6MB)
테스트 11 〉	통과 (2.11ms, 10.4MB)
테스트 12 〉	통과 (2.55ms, 10.4MB)
테스트 13 〉	통과 (2.90ms, 10.7MB)
테스트 14 〉	통과 (2.38ms, 10.4MB)
테스트 15 〉	통과 (3.46ms, 10.5MB)
테스트 16 〉	통과 (1.01ms, 10.2MB)
테스트 17 〉	통과 (0.57ms, 10.3MB)
테스트 18 〉	통과 (0.26ms, 10.1MB)
테스트 19 〉	통과 (0.06ms, 10.3MB)
테스트 20 〉	통과 (0.60ms, 10.2MB)
'''