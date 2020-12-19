import sys
sys.stdin = open('input.txt')

N, Q = map(int, input().split())
length = 2**N
matrix = [list(map(int, input().split())) for _ in range(length)]
steps = list(map(int, input().split()))

def rotate(M, l):
    tmp_matrix = [[0]*l for _ in range(l)]
    for i in range(l):
        for j in range(l):
            tmp_matrix[j][l-i-1] = M[i][j]
    return tmp_matrix

D = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, +1)
]

for L in steps:
    new_matrix = [[0]*length for _ in range(length)]
    for i in range(2**(N-L)):
        for j in range(2**(N-L)):
            micro_matrix = [[0]*2**L for _ in range(2**L)]
            for k in range(2**L):
                for l in range(2**L):
                    micro_matrix[k][l] = matrix[i*(2**L)+k][j*(2**L)+l]
            rotated_matrix = rotate(micro_matrix, 2**L)
            for k in range(2**L):
                for l in range(2**L):
                    new_matrix[i*(2**L)+k][j*(2**L)+l] = rotated_matrix[k][l]
    
    minus_ice = []
    for i in range(length):
        for j in range(length):
            if new_matrix[i][j]:
                ice = 0
                for k in range(4):
                    ni = i + D[k][0]
                    nj = j + D[k][1]
                    if 0 <= ni < length and 0 <= nj < length:
                        if new_matrix[ni][nj]:
                            ice += 1
                if not ice >= 3:
                    minus_ice.append((i, j))
    
    for i, j in minus_ice:
        new_matrix[i][j] -= 1
    matrix = new_matrix

total = 0
for i in range(length):
    total += sum(matrix[i])

max_ice = 0
def dfs(i, j, count):
    global max_ice
    for k in range(4):
        ni = i + D[k][0]
        nj = j + D[k][1]
        if 0 <= ni < length and 0 <= nj < length:
            if matrix[ni][nj]:
                matrix[ni][nj] = 0
                dfs(ni, nj, count+1)
                break
    else:
        if count > max_ice:
            max_ice = count

for i in range(length):
    for j in range(length):
        if matrix[i][j]:
            matrix[i][j] = 0
            dfs(i, j, 1)

print(total)
print(max_ice)