def solution(user_id, banned_id):
    answer = set()
    ban_length = len(banned_id)
    user_length = len(user_id)
    #벤길이과 유저길이가 같다면 경우의 수는 1개라고 리턴
    if ban_length == user_length:
        return 1
    #걸린 유저 체크용
    use_user = [1 for _ in range(user_length)]
    #사용된 벤유저 체크용
    use_ban = [1 for _ in range(ban_length)]
    #dfs를 이용하여 경우의 수를 검사
    stack = []
    #첫 시작은 0부터이다.
    stack.append([0, use_user, use_ban])
    #스택이 빌때까지 반복
    while stack:
        #스택에서 데이터를 꺼내 매칭
        idx, use_user, use_ban = stack.pop()
        #모든 벤유저를 찾았다면 정답에 추가
        #중복을 방지하기 위해 셋구조에 추가
        if idx == ban_length:
            temp = []
            for i in range(user_length):
                if not use_user[i]: temp.append(user_id[i])
            if temp: answer.add(tuple(temp))
        #벤유저와 모든 유저를 반복해서 돈다.
        for i in range(ban_length):
            #체크한 벤유저가 아니라면
            if use_ban[i] : 
                for j in range(user_length):
                    # 사용한 유저가 아니어야 하고, 벤유저아이디 길어와 유저아이디 길이가 같아야 한다.
                    if use_user[j] and len(banned_id[i]) == len(user_id[j]):
                        #반복문을 돌면서 둘이 매칭되는지 확인한다. * 인경우 넘어간다.
                        for k in range(len(user_id[j])):
                            if user_id[j][k] != banned_id[i][k] and banned_id[i][k] != '*':
                                break
                        #break가 걸리지 않았다면
                        else:
                            #유저와 벤유저 모드 체크하고
                            use_user[j] = 0
                            use_ban[i] = 0
                            #스택에 추가한다.
                            stack.append([idx+1, use_user[:], use_ban[:]])
                            #체크한것을 해제
                            use_user[j] = 1
                            use_ban[i] = 1
    #set의 길이가 경우의 수이다.
    return len(answer)