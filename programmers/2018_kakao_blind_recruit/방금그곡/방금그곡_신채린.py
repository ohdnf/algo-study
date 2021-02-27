def solution(m, musicinfos):
    def time_difference(start, end):
        diff = 0
        if end[:2] != start[:2]:
            if end[:2] - start[:2] != 1:
                diff += 60 * (end[:2]-start[:2]-1)
            diff += 60 - int(start[3:])
            diff += int(end[3:])
        else:
            diff += int(end[3:]) - int(start[3:])
        return diff
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
        return " (None) "