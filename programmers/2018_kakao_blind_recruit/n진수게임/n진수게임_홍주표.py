DIGIT = '0123456789ABCDEF'

def convert(number, base):
    quo, rem = divmod(number, base)     # quotient, remainder
    return convert(quo, base) + DIGIT[rem] if quo else DIGIT[rem]

def solution(n, t, m, p):
    numbers = ''
    curr = 0
    least_length = m * t
    while len(numbers) < least_length:
        numbers += convert(curr, n)
        curr += 1
    # print(numbers)
    return numbers[p-1:m*t:m]


"""
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.02ms, 10.2MB)
테스트 3 〉	통과 (0.02ms, 10.2MB)
테스트 4 〉	통과 (0.02ms, 10.2MB)
테스트 5 〉	통과 (0.15ms, 10.1MB)
테스트 6 〉	통과 (0.16ms, 10.1MB)
테스트 7 〉	통과 (0.16ms, 10.3MB)
테스트 8 〉	통과 (0.16ms, 10.1MB)
테스트 9 〉	통과 (0.17ms, 10.2MB)
테스트 10 〉	통과 (0.18ms, 10.2MB)
테스트 11 〉	통과 (0.17ms, 10.2MB)
테스트 12 〉	통과 (0.17ms, 10.3MB)
테스트 13 〉	통과 (0.17ms, 10.1MB)
테스트 14 〉	통과 (22.27ms, 10.2MB)
테스트 15 〉	통과 (22.33ms, 10.2MB)
테스트 16 〉	통과 (22.28ms, 10.3MB)
테스트 17 〉	통과 (1.35ms, 10.2MB)
테스트 18 〉	통과 (1.62ms, 10.3MB)
테스트 19 〉	통과 (0.48ms, 10.2MB)
테스트 20 〉	통과 (1.26ms, 10.2MB)
테스트 21 〉	통과 (6.07ms, 10.1MB)
테스트 22 〉	통과 (2.72ms, 10.2MB)
테스트 23 〉	통과 (7.99ms, 10.2MB)
테스트 24 〉	통과 (11.66ms, 10.2MB)
테스트 25 〉	통과 (9.78ms, 10.2MB)
테스트 26 〉	통과 (3.74ms, 10.2MB)
"""
