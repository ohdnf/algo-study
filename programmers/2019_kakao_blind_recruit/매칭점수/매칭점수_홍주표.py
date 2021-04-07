from collections import defaultdict
import re

# 외부 링크 매핑
EXT_LINK = defaultdict(set)

def get_url(page):
    url = page.split('<meta property=\"og:url\" content=\"https://')
    url = url[1].split('\"/>')[0]
    return url

def get_basic_point(page, q):
    idx = 0
    parsed = ''
    words = []
    while idx < len(page):
        if page[idx].isalpha():
            parsed += page[idx]
        else:
            if parsed:
                words.append(parsed.lower())
                parsed = ''
        idx += 1
    # print(q.lower(), words)
    return words.count(q.lower())

def get_link(page, url):
    count = 0
    links = page.split('<body>')[1].split('<a href=\"')
    for link in links:
        if link.startswith('https://'):
            link = link.split('\">')[0][8:]
            count += 1
            EXT_LINK[link].add(url)
    return count

def solution(word, pages):
    """
    기본점수 = 검색어 등장 횟수(대소문자 무시)
    외부 링크 수 = 다른 외부 페이지로 연결된 링크 개수
    링크점수 = (해당 웹페이지로 링크가 걸린 웹페이지의 (기본점수 / 외부 링크 수))의 총합
    매칭점수 = 기본점수 + 링크점수
    """
    # 웹페이지 정보: 인덱스, 기본점수, 외부 링크 수
    page_info = {}
    for idx, page in enumerate(pages):
        url = get_url(page)
        # print('url', url)
        page_info[url] = [idx, get_basic_point(page, word), get_link(page, url)]
    # print('page_info', page_info)
    
    # 매칭점수 구하기
    # url = 현재 웹페이지
    # link = 현재 웹페이지를 외부 링크로 갖는 웹페이지
    result = []
    for url in page_info.keys():
        link_point = 0  # 링크점수
        for link in list(EXT_LINK[url]):
            _, basic_point, num_of_link = page_info[link]
            link_point += basic_point / num_of_link
        idx, basic_point, _ = page_info[url]
        result.append([basic_point + link_point, idx])

    # 매칭점수가 가장 높은 웹페이지의 인덱스 구하기, 동점이라면 작은 번호 우선
    result.sort(key=lambda u: (-u[0], u[1]))
    return result[0][1]


"""
정확성  테스트
테스트 1 〉	통과 (4.65ms, 10.3MB)
테스트 2 〉	통과 (3.56ms, 10.2MB)
테스트 3 〉	통과 (4.29ms, 10.3MB)
테스트 4 〉	통과 (3.68ms, 10.3MB)
테스트 5 〉	통과 (4.74ms, 10.2MB)
테스트 6 〉	통과 (4.77ms, 10.3MB)
테스트 7 〉	통과 (4.36ms, 10.3MB)
테스트 8 〉	통과 (4.17ms, 10.3MB)
테스트 9 〉	통과 (5.08ms, 10.2MB)
테스트 10 〉	통과 (4.81ms, 10.4MB)
테스트 11 〉	통과 (2.04ms, 10.3MB)
테스트 12 〉	통과 (1.94ms, 10.3MB)
테스트 13 〉	통과 (2.14ms, 10.2MB)
테스트 14 〉	통과 (2.41ms, 10.3MB)
테스트 15 〉	통과 (2.77ms, 10.3MB)
테스트 16 〉	통과 (0.80ms, 10.3MB)
테스트 17 〉	통과 (2.35ms, 10.3MB)
테스트 18 〉	통과 (0.38ms, 10.4MB)
테스트 19 〉	통과 (1.14ms, 10.3MB)
테스트 20 〉	통과 (3.99ms, 10.3MB)
"""
