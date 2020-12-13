import sys
sys.stdin = open('input.txt')

import math

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

D = [
    (0, -1),
    (1, 0),
    (0, 1),
    (-1, 0)
]

result = 0
i = j = N//2
k = 0
while k < 2*N - 1:
    for idx in range(k//2 + 1):
        d = k % 4
        i = i + D[d][0] 
        j = j + D[d][1]
        if j < 0:
            break
        total = matrix[i][j]
        if not total:
            continue
        matrix[i][j] = 0
        one = math.floor(total*(1/100))
        two = math.floor(total*(2/100))
        five = math.floor(total*(5/100))
        seven = math.floor(total*(7/100))
        ten = math.floor(total*(10/100))
        alpha = total - (2*(one + two + seven + ten) + five)
        
        a = D[d][0]
        b = D[d][1]
        if 0 <= i-a+b < N and 0 <= j-b-a < N:
            matrix[i-a+b][j-b-a] += one
        else:
            result += one
        if 0 <= i-a-b < N and 0 <= j-b+a < N:
            matrix[i-a-b][j-b+a] += one
        else:
            result += one
        if 0 <= i+2*b < N and 0 <= j+2*a < N:
            matrix[i+2*b][j+2*a] += two
        else:
            result += two
        if 0 <= i-2*b < N and 0 <= j-2*a < N:
            matrix[i-2*b][j-2*a] += two
        else:
            result += two
        if 0 <= i+2*a < N and 0 <= j+2*b < N:
            matrix[i+2*a][j+2*b] += five
        else:
            result += five
        if 0 <= i+b < N and 0 <= j-a < N:
            matrix[i+b][j-a] += seven
        else:
            result += seven
        if 0 <= i-b < N and 0 <= j+a < N:
            matrix[i-b][j+a] += seven
        else:
            result += seven
        if 0 <= i+a+b < N and 0 <= j+b-a < N:
            matrix[i+a+b][j+b-a] += ten
        else:
            result += ten
        if 0 <= i+a-b < N and 0 <= j+a+b < N:
            matrix[i+a-b][j+a+b] += ten
        else:
            result += ten
        if 0 <= i+a < N and 0 <= j+b < N:
            matrix[i+a][j+b] += alpha
        else:
            result += alpha
        
    k += 1
print(result)

# 메모리 41124KB
# 시간 2012ms
