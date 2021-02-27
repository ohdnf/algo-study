def get_time(start_time, end_time):
    s_h, s_m = map(int, start_time.split(':'))
    e_h, e_m = map(int, end_time.split(':'))
    
    return (e_h - s_h) * 60 + e_m - s_m

def solution(m, musicinfos):
    answer = [0, '(None)', '']
    # make full play melodies using musicinfos
    full_melodies = []
    for musicinfo in musicinfos:
        start_time, end_time, title, melody = musicinfo.split(',')
        play_time = get_time(start_time, end_time)
        melody = melody * (play_time // len(melody)) + melody[:play_time % len(melody)]
        full_melodies.append((play_time, title, melody))
    
    # find the song matched
    matched_songs = []
    for idx, full_melody in enumerate(full_melodies):
        play_time, title, melody = full_melody
        start_idx = melody.find(m)
        if start_idx == -1:
            continue
        end_idx = start_idx + len(m)
        if end_idx > len(melody):
            continue
        if melody[end_idx] == '#':
            continue
        matched_songs.append((play_time, idx, title))
    matched_songs.sort(key=lambda s: (s[0], s[1]))
    # print('full_melodies', full_melodies)
    # print('matched_songs', matched_songs)
    if len(matched_songs) == 0:
        return '(None)'
    return matched_songs[0][2]
