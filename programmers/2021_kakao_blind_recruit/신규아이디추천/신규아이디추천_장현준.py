'''2021 카카오공채 문제1
아이디 규칙
- 길이 3 ~ 15
- 소문자, 숫자 , -, _, . 사용가능
    단 .는 처음과 끝에 사용 불가 & 연속 사용 불가
'''
def solution(new_id):
    # origin = new_id[:]
    
    # 1단계
    new_id = new_id.lower()
    # if origin == "...!@BaT#*..y.abcdefghijklm": print("...!@bat#*..y.abcdefghijklm" == new_id or new_id)
    
    # 2단계
    new_id = "".join(ch for ch in new_id
                     if 'a' <= ch <= 'z' or
                     ch in [str(i) for i in range(10)] or
                    ch in ('-', '_', '.'))
    # if origin == "...!@BaT#*..y.abcdefghijklm": print("...bat..y.abcdefghijklm" == new_id or new_id)
    
    # 3단계
    prev_len = len(new_id)
    while True:
        new_id = new_id.replace('..', '.')
        if len(new_id) == prev_len:
            break
        else:
            prev_len = len(new_id)
    # if origin == "...!@BaT#*..y.abcdefghijklm": print(".bat.y.abcdefghijklm" == new_id or new_id)

    # 4단계
    if new_id and new_id[0] == ".":
        new_id = new_id[1:]
    if new_id and new_id[-1] == ".":
        new_id = new_id[:-1]
    # if origin == "...!@BaT#*..y.abcdefghijklm": print("bat.y.abcdefghijklm" == new_id or new_id)

    # 5단계
    if not new_id:
        new_id = "a"
    # if origin == "...!@BaT#*..y.abcdefghijklm": print("bat.y.abcdefghijklm" == new_id or new_id)
        
    # 6단계
    new_id = new_id[:15]
    if new_id[-1] == ".":
        new_id = new_id[:-1]
    # if origin == "...!@BaT#*..y.abcdefghijklm": print("bat.y.abcdefghi" == new_id or new_id)
        
    # 7단계
    if len(new_id) <= 2:
        new_id += new_id[-1] * (3-len(new_id))
    # if origin == "...!@BaT#*..y.abcdefghijklm": print("bat.y.abcdefghi" == new_id or new_id)
    return new_id

'''
정확성  테스트
테스트 1 〉	통과 (0.02ms, 10.2MB)
테스트 2 〉	통과 (0.02ms, 10.4MB)
테스트 3 〉	통과 (0.03ms, 10.2MB)
테스트 4 〉	통과 (0.03ms, 10.3MB)
테스트 5 〉	통과 (0.03ms, 10.3MB)
테스트 6 〉	통과 (0.02ms, 10.4MB)
테스트 7 〉	통과 (0.03ms, 10.3MB)
테스트 8 〉	통과 (0.03ms, 10.4MB)
테스트 9 〉	통과 (0.02ms, 10.3MB)
테스트 10 〉통과 (0.02ms, 10.3MB)
테스트 11 〉통과 (0.03ms, 10.4MB)
테스트 12 〉통과 (0.04ms, 10.5MB)
테스트 13 〉통과 (0.04ms, 10.5MB)
테스트 14 〉통과 (0.03ms, 10.3MB)
테스트 15 〉통과 (0.04ms, 10.4MB)
테스트 16 〉통과 (0.06ms, 10.2MB)
테스트 17 〉통과 (0.16ms, 10.4MB)
테스트 18 〉통과 (0.22ms, 10.3MB)
테스트 19 〉통과 (0.43ms, 10.5MB)
테스트 20 〉통과 (0.42ms, 10.3MB)
테스트 21 〉통과 (0.43ms, 10.3MB)
테스트 22 〉통과 (0.41ms, 10.3MB)
테스트 23 〉통과 (0.49ms, 10.2MB)
테스트 24 〉통과 (0.29ms, 10.3MB)
테스트 25 〉통과 (0.49ms, 10.3MB)
테스트 26 〉통과 (0.47ms, 10.3MB)
'''