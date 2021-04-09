'''
기본점수: 검색어 등장 횟수 (대소문자 구분x)
외부 링크 수: 나가는 링크 수
링크 점수: 들어오는 링크 => 웹페이지의 <기본점수 / 외부 링크 수>
매칭 점수: 기본점수 + 링크점수

입력
- word: 1~12 단어, 알파벳
    - 단어 단위 매칭
- pages: 1~20배열, 각 1~1500길이
    - 총 30,000길이
    - url: https://로시작한다.
        - 해당 페이지 url: head > meta 태그의 값으로 주어진다.
        - 외부 링크 url: <a href="링크"\> 형태
            - a태그 내 다른 attribute 주어지는 경우는 없다. 
출력
- 
- 
'''
from collections import defaultdict

def solution(word, pages):

    def check_tag(tag, cur_page_name, out_link): # cur_page_name는 리턴, out_link는 객체참조하여 직접 append
        temp = tag.strip().split()
        tag_name = temp[0].lower()
        
        # 내 주소 찾기
        if tag_name == "meta":
            if not cur_page_name:            
                for word in temp[1:]: # attribute
                    attr_name, value = word.split("=")
                    
                    attr_name = attr_name.lower()
                    if attr_name == "content":
                        while value[-1] != '\"':
                            value = value[:-1]
                        cur_page_name = (value[1:-1])
                        break
                    
        # a태그는 항상 href만 포함
        elif tag_name == "a": 
            for word in temp[1:]:
                attr_name, value = word.split("=")
                attr_name = attr_name.lower()
                if attr_name == "href":
                    while value[-1] != '\"':
                        value = value[:-1]
                    out_link.append(value[1:-1]) # out_link에 찾은 주소 추가
                    break
                    
        return cur_page_name
    
    def check_word(st):
        return len(st) == len(word) and st.lower() == word
        
    word = word.lower() 
    web_pages = dict()
    
    for page_index, page in enumerate(pages):
        
        page = page.replace('\t', ' ')
        page = page.replace('\n', ' ')
        
        mode = 0 # 0:기본, 1:태그, 2:단어수집, 3: 실패중
        temp = ""
        out_link = []
        cur_page_name = ""
        basic_score = 0
        
        for i in range(len(page)):
            ch = page[i]
            
            # tag 수집 완료
            if ch == ">":
                cur_page_name = check_tag(temp, cur_page_name, out_link)
                temp = ""
                mode = 0
                continue
            
            # 1: tag 수집 모드
            if mode == 1: 
                temp += ch
                continue
                
            # 1. 알파벳 O
            if "a" <= ch <= "z" or "A" <= ch <= "Z":
                if mode != 3:
                    if(mode == 2 and len(temp) == len(word)): # 단어길이 초과
                        mode = 3
                    else:
                        temp += ch # 단어수집 계속 | 시작
                        mode = 2 if mode != 2 else mode
            else:
            # 2. 알파벳 X
                if mode == 2: # 수집하던 단어 확인
                    basic_score += check_word(temp)
                temp = ""
                mode = 1 if ch == "<" else 0 # `<`면 tag 수집 모드 활성화
        web_pages[cur_page_name] = {
            'index': page_index,
            'basic_score': basic_score,
            'total_score': basic_score,  # 여기에 나중에 out_links에 의한 값 추가하면 됨
            'out_links': out_link,
        }

    for page_name in web_pages.keys():
        # 각 페이지의 out_score 계산
        links = web_pages[page_name]['out_links']
        if len(links) == 0: continue
        out_score = web_pages[page_name]['basic_score'] / len(links)
        # 해당 링크가 가르키는 주소에 점수 추가
        for link in links:
            if link in web_pages:
                web_pages[link]['total_score'] += out_score
    
    # 매칭 점수 최대인 웹페이지 인덱스 리턴
    max_v = -1
    max_i = -1
    for page_name in web_pages.keys():
        if max_v < web_pages[page_name]['total_score']:
            max_v, max_i = web_pages[page_name]['total_score'], web_pages[page_name]['index']
    return max_i


"""
정확성  테스트
테스트 1 〉	통과 (3.43ms, 10.3MB)
테스트 2 〉	통과 (2.43ms, 10.4MB)
테스트 3 〉	통과 (3.03ms, 10.3MB)
테스트 4 〉	통과 (3.02ms, 10.4MB)
테스트 5 〉	통과 (3.80ms, 10.5MB)
테스트 6 〉	통과 (3.32ms, 10.5MB)
테스트 7 〉	통과 (5.08ms, 10.3MB)
테스트 8 〉	통과 (2.93ms, 10.3MB)
테스트 9 〉	통과 (3.73ms, 10.4MB)
테스트 10 〉통과 (3.24ms, 10.3MB)
테스트 11 〉통과 (2.29ms, 10.4MB)
테스트 12 〉통과 (4.26ms, 10.4MB)
테스트 13 〉통과 (2.24ms, 10.4MB)
테스트 14 〉통과 (2.38ms, 10.3MB)
테스트 15 〉통과 (2.18ms, 10.3MB)
테스트 16 〉통과 (0.79ms, 10.4MB)
테스트 17 〉통과 (1.76ms, 10.3MB)
테스트 18 〉통과 (0.34ms, 10.3MB)
테스트 19 〉통과 (0.97ms, 10.3MB)
테스트 20 〉통과 (2.24ms, 10.4MB)
"""
