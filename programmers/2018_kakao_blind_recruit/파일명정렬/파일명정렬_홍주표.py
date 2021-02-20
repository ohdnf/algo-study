def solution(files):
    answer = []
    # file ==> HEAD + NUMBER + TAIL
    for _file in files:
        cur = 0
        for idx, cha in enumerate(_file):
            if cha.isdigit():
                break
            else:
                cur += 1
        head = _file[:cur]
        bef = cur
        for idx in range(cur, len(_file)):
            if _file[idx].isdigit():
                cur += 1
            else:
                break
        number = _file[bef:cur]
        tail = _file[cur:]
        answer.append((head.lower(), int(number), _file))
    answer = [_file for _, _, _file in sorted(answer, key=lambda f: (f[0], f[1]))]
    return answer

"""
테스트 1 〉	통과 (0.05ms, 10.4MB)
테스트 2 〉	통과 (0.04ms, 10.4MB)
테스트 3 〉	통과 (2.99ms, 10.7MB)
테스트 4 〉	통과 (2.75ms, 10.7MB)
테스트 5 〉	통과 (2.87ms, 10.7MB)
테스트 6 〉	통과 (2.97ms, 10.7MB)
테스트 7 〉	통과 (2.89ms, 10.7MB)
테스트 8 〉	통과 (2.67ms, 10.6MB)
테스트 9 〉	통과 (2.75ms, 10.6MB)
테스트 10 〉	통과 (2.74ms, 10.7MB)
테스트 11 〉	통과 (2.86ms, 10.7MB)
테스트 12 〉	통과 (2.78ms, 10.7MB)
테스트 13 〉	통과 (2.46ms, 10.7MB)
테스트 14 〉	통과 (2.86ms, 10.9MB)
테스트 15 〉	통과 (4.29ms, 10.8MB)
테스트 16 〉	통과 (2.82ms, 10.7MB)
테스트 17 〉	통과 (2.47ms, 10.7MB)
테스트 18 〉	통과 (2.58ms, 10.7MB)
테스트 19 〉	통과 (2.71ms, 10.7MB)
테스트 20 〉	통과 (2.69ms, 10.6MB)
"""