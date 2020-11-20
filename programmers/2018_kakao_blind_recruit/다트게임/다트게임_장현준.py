def solution(dartResult):
    # 총 3번의 기회 => 0 ~ 30점
    # 점수
    # S, D, T, *:2배, #:-
    
    number = "" # "0" ~ "10"
    point = []
    def sdt (number, command):
        if command == "S":
            return int(number)
        if command == "D":
            return int(number) ** 2
        if command == "T":
            return int(number) ** 3
    def option(point, command):
        if command == "#":
            point[-1] = (-1 * point[-1])
        else:
            point[-1] *= 2
            if len(point) != 1:
                point[-2] *= 2
    # 1. 문자열을 처음부터 끝까지 1개씩 탐색한다.
    for ch in dartResult:
        # 2. 하나의 다트는 숫자로 시작해서 다음 숫자 or 끝에서 끝난다.
        if ch in "*#": # 4. 매 옵션마다 점수들을 반영한다.
            option(point, ch)
        elif ch in "SDT": # 3. 숫자 & 영역으로 점수를 먼저 구한다.
            point.append(sdt(number, ch))
            number = ""
        # elif "0" <= ch <= "10":
        else:
            number += ch
    return sum(point)

# 테스트 1 〉	통과 (0.03ms, 10.4MB)
# 테스트 2 〉	통과 (0.02ms, 10.3MB)
# 테스트 3 〉	통과 (0.03ms, 10.4MB)
# 테스트 4 〉	통과 (0.02ms, 10.3MB)
# 테스트 5 〉	통과 (0.03ms, 10.3MB)
# 테스트 6 〉	통과 (0.02ms, 10.4MB)
# 테스트 7 〉	통과 (0.02ms, 10.4MB)
# 테스트 8 〉	통과 (0.03ms, 10.4MB)
# 테스트 9 〉	통과 (0.03ms, 10.4MB)
# 테스트 10 〉통과 (0.03ms, 10.3MB)
# 테스트 11 〉통과 (0.02ms, 10.3MB)
# 테스트 12 〉통과 (0.02ms, 10.4MB)
# 테스트 13 〉통과 (0.02ms, 10.4MB)
# 테스트 14 〉통과 (0.03ms, 10.4MB)
# 테스트 15 〉통과 (0.03ms, 10.3MB)
# 테스트 16 〉통과 (0.03ms, 10.4MB)
# 테스트 17 〉통과 (0.02ms, 10.3MB)
# 테스트 18 〉통과 (0.02ms, 10.3MB)
# 테스트 19 〉통과 (0.03ms, 10.4MB)
# 테스트 20 〉통과 (0.03ms, 10.3MB)
# 테스트 21 〉통과 (0.03ms, 10.3MB)
# 테스트 22 〉통과 (0.02ms, 10.3MB)
# 테스트 23 〉통과 (0.03ms, 10.5MB)
# 테스트 24 〉통과 (0.03ms, 10.4MB)
# 테스트 25 〉통과 (0.03ms, 10.4MB)
# 테스트 26 〉통과 (0.03ms, 10.4MB)
# 테스트 27 〉통과 (0.03ms, 10.3MB)
# 테스트 28 〉통과 (0.02ms, 10.3MB)
# 테스트 29 〉통과 (0.03ms, 10.4MB)
# 테스트 30 〉통과 (0.03ms, 10.4MB)
# 테스트 31 〉통과 (0.03ms, 10.3MB)
# 테스트 32 〉통과 (0.03ms, 10.3MB)