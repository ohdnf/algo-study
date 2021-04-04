from collections import defaultdict

LINKS = defaultdict(set)

def get_url(page):
    url = page.split('<meta property=\"og:url\" content=\"https://')
    url = url[1].split('\"/>')[0]
    return url

def get_basic_point(page):
    basic_point = 0
    return basic_point

def get_num_of_link(page, url):
    num_of_link = 0
    links = page.split('<body>')[1].split('<a href=')
    for link in links:
        link = link.split('>')[0].strip('"')
        num_of_link += 1
        LINKS[link].add(url)
    return num_of_link

def get_link_point(page):
    num_of_link = 0
    url_of_links = []
    links = page.split('<body>')[1].split('<a href=')
    for link in links:
        link = link.split('>')[0].strip('"')
        num_of_link += 1
        
    return link_point

def solution(word, pages):
    result = []
    for idx, page in enumerate(pages):
        url = get_url(page)
        print(url)
        # basic_point = get_basic_point(page)
        # num_of_link = get_num_of_link(page, url)
        # result.append((idx, ))
    
    
