def solution(new_id):
    import re
    
     # 1단계
    revised_id = new_id.lower()
    
    # 2단계 + 3단계
    com = re.compile('[a-z0-9-_.]')
    characters = com.findall(revised_id)
    revised_id = ''
    pre_full_stop = False
    for character in characters:
        if character == '.':
            if pre_full_stop:
                continue
            else:
                pre_full_stop = True
        else:
            pre_full_stop = False
        revised_id += character
    
    # 4단계
    revised_id = revised_id.strip('.')
    
    # 5단계
    if not revised_id:
        revised_id = 'a'
    
    # 6단계
    revised_id = revised_id[:15].strip('.')
    
    # 7단계
    if len(revised_id) <= 2:
        revised_id += revised_id[-1] * (3 - len(revised_id))
    
    return revised_id

'''
테스트 1 〉	통과 (0.41ms, 10.2MB)
테스트 2 〉	통과 (0.12ms, 10.1MB)
테스트 3 〉	통과 (0.13ms, 10.2MB)
테스트 4 〉	통과 (0.12ms, 10.2MB)
테스트 5 〉	통과 (0.13ms, 10.2MB)
테스트 6 〉	통과 (0.13ms, 10.1MB)
테스트 7 〉	통과 (0.13ms, 10.3MB)
테스트 8 〉	통과 (0.13ms, 10.2MB)
테스트 9 〉	통과 (0.12ms, 10.2MB)
테스트 10 〉	통과 (0.12ms, 10.2MB)
테스트 11 〉	통과 (0.13ms, 10.3MB)
테스트 12 〉	통과 (0.13ms, 10.2MB)
테스트 13 〉	통과 (0.13ms, 10.3MB)
테스트 14 〉	통과 (0.13ms, 10.2MB)
테스트 15 〉	통과 (0.13ms, 10.1MB)
테스트 16 〉	통과 (0.14ms, 10.2MB)
테스트 17 〉	통과 (0.20ms, 10.3MB)
테스트 18 〉	통과 (0.26ms, 10.2MB)
테스트 19 〉	통과 (0.40ms, 10.3MB)
테스트 20 〉	통과 (0.15ms, 10.1MB)
테스트 21 〉	통과 (0.24ms, 10.3MB)
테스트 22 〉	통과 (0.14ms, 10.3MB)
테스트 23 〉	통과 (0.38ms, 10.2MB)
테스트 24 〉	통과 (0.46ms, 10.2MB)
테스트 25 〉	통과 (0.33ms, 10.2MB)
테스트 26 〉	통과 (0.34ms, 10.2MB)
'''