def solution(word, pages):
    # 1. meta tag 걸려 있는 녀석 중 content에 담겨져 있는 녀석 뽑아내기 => page의 url
    # 2. href 있는 부분 찾아내기 => page의 외부링크
    # 3. body 안에 태그를 제외한 부분 이외에서 word 찾기(알파벳 아닌 걸로 split 해야함)
    # 4. sorting
    import re
    from html.parser import HTMLParser
    infos = []
    info = {
        'start': [],
        'data': []
    }

    word = word.lower()

    class MyHTMLParser(HTMLParser):
        def handle_starttag(self, tag, attrs):
            info['start'].append([tag, attrs])

        def handle_data(self, data):
            data = data.strip()
            if (data):
                info['data'].append(data.lower())

    parser = MyHTMLParser()
    for page in pages:
        parser.feed(page)
        infos.append(info)
        info = {
        'start': [],
        'data': []
    }

    real_infos = []
    for info in infos:
        real_info = {
            'self_url': '',
            'out_urls': [],
            'matched_words': 0
        }
        starts = info['start']
        for start in starts:
            tag = start[0]
            attrs = start[1]
            if tag == 'meta':
                for attr in attrs:
                    if attr[0] == 'content':
                        real_info['self_url'] = attr[1]
                        break
            if tag == 'a':
                for attr in attrs:
                    if attr[0] == 'href':
                        real_info['out_urls'].append(attr[1])

        datas = info['data']
        for data in datas:
            words = re.split("[^a-z]",data)
            for c_word in words:
                if c_word == word:
                    real_info['matched_words'] += 1
        
        real_infos.append(real_info)

    for i in range(len(real_infos)):
        current_node = real_infos[i]
        matching_score = current_node['matched_words']

        for j in range(len(real_infos)):
            if i != j:
                other_node = real_infos[j]
                if current_node['self_url'] in other_node['out_urls']:
                    matching_score += other_node['matched_words'] / len(other_node['out_urls'])
        real_infos[i]['matching_score'] = matching_score
    
    max_ms = 0
    answer = 0
    for i in range(len(real_infos)):
        if real_infos[i]['matching_score'] > max_ms:
            max_ms = real_infos[i]['matching_score']
            answer = i
    return answer

print(solution('Muzi', ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]))

'''
테스트 1 〉	통과 (168.53ms, 11MB)
테스트 2 〉	통과 (9.27ms, 11MB)
테스트 3 〉	통과 (39.75ms, 11MB)
테스트 4 〉	통과 (7.26ms, 11MB)
테스트 5 〉	통과 (8.51ms, 11MB)
테스트 6 〉	통과 (8.81ms, 11.1MB)
테스트 7 〉	통과 (7.60ms, 11MB)
테스트 8 〉	통과 (6.95ms, 11MB)
테스트 9 〉	통과 (8.38ms, 11.1MB)
테스트 10 〉	통과 (7.84ms, 11.1MB)
테스트 11 〉	통과 (5.48ms, 10.9MB)
테스트 12 〉	통과 (5.05ms, 10.9MB)
테스트 13 〉	통과 (5.83ms, 11MB)
테스트 14 〉	통과 (6.61ms, 11MB)
테스트 15 〉	통과 (6.15ms, 10.9MB)
테스트 16 〉	통과 (4.50ms, 10.9MB)
테스트 17 〉	통과 (6.58ms, 11MB)
테스트 18 〉	통과 (4.41ms, 10.9MB)
테스트 19 〉	통과 (4.61ms, 10.9MB)
테스트 20 〉	통과 (7.35ms, 11MB)
'''