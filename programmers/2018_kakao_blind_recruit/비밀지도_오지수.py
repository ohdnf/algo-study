def make_binary(num, length):
    result = [' ']*length
    for i in range(length):
        if num % 2:
            result[-i-1] = '#'
        num = num//2
    return result


def solution(n, arr1, arr2):
    data = [['']*n for _ in range(n)]
    for i in range(n):
        arr1_binary = make_binary(arr1[i], n)
        arr2_binary = make_binary(arr2[i], n)
        data[i] = ['#' if '#' in a+b else ' ' for a, b in zip(arr1_binary, arr2_binary)]
    answer = ["".join(data[i]) for i in range(n)]
    return answer
