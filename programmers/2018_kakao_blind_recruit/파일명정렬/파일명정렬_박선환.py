def solution(files):
    answer = []
    copy = []
    for i in range(len(files)):
        copy.append([files[i].lower(), i])
    
    import re
    head_r = re.compile('[^0-9]+')
    number_r = re.compile('[0-9]+')
    for i in range(len(copy)):
        head = head_r.findall(copy[i][0])
        if len(head):
            copy[i].append(head[0])
        else:
            copy[i].append('')
        
        number = number_r.findall(copy[i][0])
        if len(number):
            copy[i].append(int(number[0]))
        else:
            copy[i].append(0)
    
    copy.sort(key=lambda x: x[3])
    copy.sort(key=lambda x: x[2])
    for file in copy:
        answer.append(files[file[1]])
    
    return answer

'''
테스트 1 〉	통과 (0.22ms, 10.4MB)
테스트 2 〉	통과 (0.21ms, 10.4MB)
테스트 3 〉	통과 (3.10ms, 10.6MB)
테스트 4 〉	통과 (3.18ms, 10.8MB)
테스트 5 〉	통과 (3.08ms, 10.6MB)
테스트 6 〉	통과 (2.83ms, 10.7MB)
테스트 7 〉	통과 (2.89ms, 10.7MB)
테스트 8 〉	통과 (2.77ms, 10.6MB)
테스트 9 〉	통과 (2.73ms, 10.6MB)
테스트 10 〉	통과 (2.79ms, 10.7MB)
테스트 11 〉	통과 (2.79ms, 10.6MB)
테스트 12 〉	통과 (3.23ms, 10.6MB)
테스트 13 〉	통과 (2.88ms, 10.6MB)
테스트 14 〉	통과 (3.61ms, 10.9MB)
테스트 15 〉	통과 (3.68ms, 10.9MB)
테스트 16 〉	통과 (2.72ms, 10.6MB)
테스트 17 〉	통과 (2.75ms, 10.8MB)
테스트 18 〉	통과 (2.65ms, 10.7MB)
테스트 19 〉	통과 (2.80ms, 10.7MB)
테스트 20 〉	통과 (4.28ms, 10.7MB)
'''