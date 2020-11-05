def solution(n, arr1, arr2):
    def to_binary(num):
        result = ''
        while num:
            num, rest = divmod(num, 2)
            result = str(rest) + result
        result = '0'*(n - len(result)) + result
        return result
    arr1 = list(map(to_binary, arr1))
    arr2 = list(map(to_binary, arr2))
    answer = []
    for i in range(n):
        temp = ''
        for j in range(n):
            if arr1[i][j] == '1' or arr2[i][j] == '1':
                temp = temp + '#'
            else:
                temp = temp + ' '
        answer.append(temp)
    return answer