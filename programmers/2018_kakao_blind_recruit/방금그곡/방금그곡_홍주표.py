def get_time(start_time, end_time):
    s_h, s_m = map(int, start_time.split(':'))
    e_h, e_m = map(int, end_time.split(':'))
    
    return (e_h - s_h) * 60 + e_m - s_m

def change_code(melody):
    for code in ('C#', 'D#', 'F#', 'G#', 'A#'):
        melody = melody.replace(code, code[0].lower())
    return melody

def solution(m, musicinfos):
    # make full play melodies using musicinfos
    full_melodies = []
    for musicinfo in musicinfos:
        start_time, end_time, title, melody = musicinfo.split(',')
        melody = change_code(melody)
        play_time = get_time(start_time, end_time)
        melody = melody * (play_time // len(melody)) + melody[:play_time % len(melody)]
        full_melodies.append((play_time, title, melody))
    
    # find the song matched
    matched_songs = []
    for idx, full_melody in enumerate(full_melodies):
        play_time, title, melody = full_melody
        m = change_code(m)
        start_idx = melody.find(m)
        if start_idx == -1:
            continue
        end_idx = start_idx + len(m)
        if end_idx > len(melody):
            continue
        matched_songs.append((play_time, idx, title))
    matched_songs.sort(key=lambda s: (-s[0], s[1]))
    # print('full_melodies', full_melodies)
    # print('matched_songs', matched_songs)
    if len(matched_songs) == 0:
        return '(None)'
    return matched_songs[0][2]

"""
테스트 1 〉	통과 (0.06ms, 10.5MB)
테스트 2 〉	통과 (0.06ms, 10.3MB)
테스트 3 〉	통과 (0.05ms, 10.2MB)
테스트 4 〉	통과 (0.06ms, 10.5MB)
테스트 5 〉	통과 (0.05ms, 10.4MB)
테스트 6 〉	통과 (0.76ms, 10.4MB)
테스트 7 〉	통과 (0.17ms, 10.5MB)
테스트 8 〉	통과 (0.16ms, 10.5MB)
테스트 9 〉	통과 (0.17ms, 10.5MB)
테스트 10 〉	통과 (0.19ms, 10.5MB)
테스트 11 〉	통과 (0.16ms, 10.4MB)
테스트 12 〉	통과 (0.17ms, 10.5MB)
테스트 13 〉	통과 (0.77ms, 10.5MB)
테스트 14 〉	통과 (1.62ms, 10.4MB)
테스트 15 〉	통과 (0.97ms, 10.5MB)
테스트 16 〉	통과 (0.76ms, 10.5MB)
테스트 17 〉	통과 (0.17ms, 10.5MB)
테스트 18 〉	통과 (0.17ms, 10.5MB)
테스트 19 〉	통과 (0.82ms, 10.5MB)
테스트 20 〉	통과 (0.18ms, 10.5MB)
테스트 21 〉	통과 (0.17ms, 10.5MB)
테스트 22 〉	통과 (0.15ms, 10.5MB)
테스트 23 〉	통과 (0.17ms, 10.5MB)
테스트 24 〉	통과 (0.16ms, 10.5MB)
테스트 25 〉	통과 (0.05ms, 10.4MB)
테스트 26 〉	통과 (0.07ms, 10.5MB)
테스트 27 〉	통과 (0.06ms, 10.5MB)
테스트 28 〉	통과 (0.06ms, 10.4MB)
테스트 29 〉	통과 (1.83ms, 10.4MB)
테스트 30 〉	통과 (1.72ms, 10.5MB)
"""
