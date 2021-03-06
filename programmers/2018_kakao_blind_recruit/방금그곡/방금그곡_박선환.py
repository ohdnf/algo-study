def solution(m, musicinfos):
    import datetime
    import numpy as np
    import re
    new_infos = []
    for music in musicinfos:
        music = music.split(',')
        music[0] = datetime.datetime.strptime(music[0], '%H:%M')
        music[1] = datetime.datetime.strptime(music[1], '%H:%M')
        duration = int((music[1] - music[0]).seconds / 60)
        music.append(duration)
        music[3] = music[3]*music[4]
        temp = ''
        pointer = 0
        for _ in range(music[4]):
            if music[3][pointer+1] == '#':
                temp += music[3][pointer:pointer+2]
                pointer += 2
            else:
                temp += music[3][pointer]
                pointer += 1
        music[3] = temp
        p = re.compile(m)
        p2 = re.compile(m+'#')
        s = p.findall(music[3])
        s2 = p2.findall(music[3])
        if s and len(s) > len(s2):
            new_infos.append(music)
    new_infos.sort(key=lambda x : x[4], reverse=True)
    if len(new_infos):
        return new_infos[0][2]
    else:
        return "(None)"


#######################
def solution(m, musicinfos):
    import datetime
    import numpy as np
    import re
    new_infos = []
    for music in musicinfos:
        music = music.split(',')
        music[0] = datetime.datetime.strptime(music[0], '%H:%M')
        music[1] = datetime.datetime.strptime(music[1], '%H:%M')
        duration = int((music[1] - music[0]).seconds / 60)
        music.append(duration)
        music[3] = music[3]*music[4]
        temp = ''
        pointer = 0
        for _ in range(music[4]):
            if music[3][pointer+1] == '#':
                temp += music[3][pointer:pointer+2]
                pointer += 2
            else:
                temp += music[3][pointer]
                pointer += 1
        music[3] = temp
        temp_num = 0
        p = re.compile(m)
        candidates = p.finditer(music[3])
        for candidate in candidates:
            try:
                if music[3][candidate.end()] != '#':
                    temp_num += 1
            except:
                temp_num += 1
        if temp_num:
            new_infos.append(music)
    new_infos.sort(key=lambda x : x[4], reverse=True)
    if len(new_infos):
        return new_infos[0][2]
    else:
        return "(None)"