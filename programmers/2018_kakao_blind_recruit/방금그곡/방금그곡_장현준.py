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
    max_length = -1
    
    print(infos)
    m = replace_shap(m)
    for play_time, title, listen_melody in infos:
        if m in listen_melody and play_time > max_length:
            answer = title
    return answer
