def solution(m, musicinfos):
    # 음: 12종류, 1분씩 재생,
    # 음악: 처음부터 재생, 종료타임 기준 반복 재생 | 종료
    # ~23:59
    # 재생시간 & 멜로디로 음악 구분 => 여러 개 => 재생 시간 긴 것
    
    # 입력
    # 1. m : 타겟멜로디, 크기: 1~1439, string 형식
    # 2. musicinfos: 크기: ~100, "시작시각,끝난시간,제목,멜로디"
        # 시각: string형식, HH:MM 형식
        # 제목: string형식, 크기: 1~64
        # 멜로디: string형식, 크기: 1~1439 
    
    # 타겟멜로디 => 각 음악
    # 1. 포함여부
    # 2. 긴 재생 시간 음악 저장
    
    def cal_play_time(start_time, end_time):
        return (int(end_time[:2]) - int(start_time[:2])) * 60 + (int(end_time[-2:]) - int(start_time[-2:]))
    
    def cal_listen_melody(play_time, melody):
        melody = replace_shap(melody) 
        return melody * (play_time // len(melody)) + melody[:play_time % len(melody)]
    
    def replace_shap(melody):
        for ch in ("C","D","F","G","A"):
            melody = melody.replace(ch+"#", ch.lower())
        return melody
    
    def pre_process(info):
        start_time, end_time, title, melody = info.split(",")
        play_time = cal_play_time(start_time, end_time)
        listen_melody = cal_listen_melody(play_time, melody)
        return play_time, title, listen_melody
    
    infos = list(map(pre_process, musicinfos))
    
    answer = "(None)"
    max_play_time = -1
    
    print(infos)
    m = replace_shap(m)
    for play_time, title, listen_melody in infos:
        if m in listen_melody and play_time > max_play_time:
            answer = title
            max_play_time = play_time
    return answer
테스트 1 〉	통과 (0.05ms, 10.4MB)
# 테스트 2 〉	통과 (0.05ms, 10.4MB)
# 테스트 3 〉	통과 (0.05ms, 10.4MB)
# 테스트 4 〉	통과 (0.06ms, 10.5MB)
# 테스트 5 〉	통과 (0.06ms, 10.4MB)
# 테스트 6 〉	통과 (0.11ms, 10.5MB)
# 테스트 7 〉	통과 (0.14ms, 10.5MB)
# 테스트 8 〉	통과 (0.14ms, 10.5MB)
# 테스트 9 〉	통과 (0.14ms, 10.5MB)
# 테스트 10 〉	통과 (0.14ms, 10.5MB)
# 테스트 11 〉	통과 (0.13ms, 10.5MB)
# 테스트 12 〉	통과 (0.14ms, 10.5MB)
# 테스트 13 〉	통과 (0.14ms, 10.5MB)
# 테스트 14 〉	통과 (0.16ms, 10.6MB)
# 테스트 15 〉	통과 (0.14ms, 10.5MB)
# 테스트 16 〉	통과 (0.16ms, 10.5MB)
# 테스트 17 〉	통과 (0.10ms, 10.5MB)
# 테스트 18 〉	통과 (0.14ms, 10.6MB)
# 테스트 19 〉	통과 (0.16ms, 10.5MB)
# 테스트 20 〉	통과 (0.14ms, 10.5MB)
# 테스트 21 〉	통과 (0.13ms, 10.5MB)
# 테스트 22 〉	통과 (0.14ms, 10.6MB)
# 테스트 23 〉	통과 (0.15ms, 10.5MB)
# 테스트 24 〉	통과 (0.14ms, 10.6MB)
# 테스트 25 〉	통과 (0.05ms, 10.4MB)
# 테스트 26 〉	통과 (0.08ms, 10.5MB)
# 테스트 27 〉	통과 (0.08ms, 10.5MB)
# 테스트 28 〉	통과 (0.06ms, 10.5MB)
# 테스트 29 〉	통과 (1.82ms, 10.5MB)
# 테스트 30 〉	통과 (1.72ms, 10.5MB)
