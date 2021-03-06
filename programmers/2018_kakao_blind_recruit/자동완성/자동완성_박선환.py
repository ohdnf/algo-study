def solution(words):
    # 1. 단어들을 연결된 dict로 한 글자씩 쪼개 담는다.
    # 2. 단어들을 돌면서 연결된 dict를 타고 들어가면서 다음 단계의 dict element가 없거나 하나만 있는 경우에 스탑시킨다. 이 때 들어간 깊이를 answer에 더해준다.
    dictionary = dict()
    for word in words:
        temp_dict = dictionary
        for i in range(len(word)):
            try:
                temp_dict = temp_dict[word[i]]
                temp_dict['has_another'] = True
            except:
                temp_dict[word[i]] = dict()
                temp_dict = temp_dict[word[i]]
                temp_dict['has_another'] = False
    
    answer = 0       
    for word in words:
        cnt = 0
        temp_dict = dictionary
        while cnt < len(word):
            temp_dict = temp_dict[word[cnt]]
            if len(temp_dict) <= 2 and not temp_dict['has_another']:
                break
            if cnt + 1 >= len(word):
                break
            cnt += 1
        answer += (cnt + 1)
    
    return answer