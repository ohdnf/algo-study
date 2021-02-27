def solution(m, musicinfos):
    def time_difference(start, end):
        start_h = int(start[:2])
        start_m = int(start[3:])
        end_h = int(end[:2])
        end_m = int(end[3:])
        return end_m - start_m + (end_h - start_h) * 60
    

    def change_code(music):
        music = music.replace('C#', 'c')
        music = music.replace('D#', 'd')
        music = music.replace('F#', 'f')
        music = music.replace('G#', 'g')
        music = music.replace('A#', 'a')
        return music
        
    answers = []
    
    m = change_code(m)
    
    for idx, musicinfo in enumerate(musicinfos):
        start, end, title, score = musicinfo.split(',')
        # 시간 차이 구하기 
        time = time_difference(start, end)
        # 악보 정보 먼저 변환하기
        score = change_code(score)
        # 악보정보 늘리기 (악보 정보 길이가 시간보다 짧으면)
        while len(score) < time:
            score += score

        score = score[:time]
        # 악보에 기억한 멜로디가 있는지 확인하기
        if m in score:
            answers.append([time, idx, title])
    
    if len(answers) != 0:
        answer = sorted(answers, key = lambda x: (-x[0], x[1]))
        return answer[0][2]
    else:
        return "(None)"

'''
테스트 1 〉	통과 (0.04ms, 10.5MB)
테스트 2 〉	통과 (0.03ms, 10.4MB)
테스트 3 〉	통과 (0.04ms, 10.4MB)
테스트 4 〉	통과 (0.03ms, 10.4MB)
테스트 5 〉	통과 (0.03ms, 10.4MB)
테스트 6 〉	통과 (0.04ms, 10.4MB)
테스트 7 〉	통과 (0.09ms, 10.5MB)
테스트 8 〉	통과 (0.09ms, 10.4MB)
테스트 9 〉	통과 (0.09ms, 10.6MB)
테스트 10 〉	통과 (0.10ms, 10.4MB)
테스트 11 〉	통과 (0.09ms, 10.4MB)
테스트 12 〉	통과 (0.09ms, 10.4MB)
테스트 13 〉	통과 (0.10ms, 10.5MB)
테스트 14 〉	통과 (0.09ms, 10.4MB)
테스트 15 〉	통과 (0.09ms, 10.4MB)
테스트 16 〉	통과 (0.12ms, 10.6MB)
테스트 17 〉	통과 (0.09ms, 10.4MB)
테스트 18 〉	통과 (0.10ms, 10.5MB)
테스트 19 〉	통과 (0.10ms, 10.5MB)
테스트 20 〉	통과 (0.09ms, 10.4MB)
테스트 21 〉	통과 (0.09ms, 10.4MB)
테스트 22 〉	통과 (0.09ms, 10.5MB)
테스트 23 〉	통과 (0.09ms, 10.5MB)
테스트 24 〉	통과 (0.09ms, 10.5MB)
테스트 25 〉	통과 (0.03ms, 10.4MB)
테스트 26 〉	통과 (0.05ms, 10.5MB)
테스트 27 〉	통과 (0.05ms, 10.5MB)
테스트 28 〉	통과 (0.04ms, 10.5MB)
테스트 29 〉	통과 (1.59ms, 10.5MB)
테스트 30 〉	통과 (1.47ms, 10.5MB)
'''