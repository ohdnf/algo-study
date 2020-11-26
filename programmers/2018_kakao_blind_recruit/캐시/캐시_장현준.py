def solution(cacheSize, cities):
    # 입력
        # 캐시크기: 정수, 0~30
        # 도시이름 배열: 문자열, 최대100,000도시, 대소문자X인 영문자, 최대 20글자
    # 7:37  캐시 크기 => 실행시간 측정 프로그램
    '''
    제주 팡요 서울
    뉴욕 팡요 서울 0
    뉴욕 엘에이 서울 1
    뉴욕 엘에이 제주 2
    팡요 엘에이 제주
    팡요 서울 제주
    팡요 서울 뉴욕
    엘에니 서울 뉴욕
    
    '''
    # 캐쉬 채워지기전
    # 1. 새로운거 => cache miss => len(cache)에 매꾸기
    # 2. 있던거 => cache hit => n 표시
    # 캐쉬 채워진후 (삭제 발생)
    # 1. 새로운거 => cache miss & 어느 자리에 매꿀지
    # 2. 있던거 => cache hit & n 표시
    if cacheSize == 0: return 5 * len(cities)
    cache = [""]*cacheSize
    log = [x for x in range(-cacheSize,0)]
    answer = 0
    for n, city in enumerate(cities):
        # 1. 있던거
        city = city.lower()
        if city in cache:
            answer += 1
            log[cache.index(city)] = n
        else:
            # 2. 새로운거
            answer += 5
            min_value = min(log)
            min_index = log.index(min_value)
            cache[min_index] = city
            log[min_index] = n
    return answer