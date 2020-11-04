# 1차 시도
def solution(n, arr1, arr2):
    arr = [[0]* n for _ in range(n)]
    list1 = []
    list2 = []
    for num in arr1:
        remain = ""
        # 이진수 구하기
        for i in range(n):
            remain = str(num % 2) + remain
            num //= 2
        # string을 리스트로 만들기
        list1.append(list(map(int, list(remain))))
            
        
    for num in arr2:
        remain = ""
        # 이진수 구하기
        for i in range(n):
            remain = str(num % 2) + remain
            num //= 2
        # string을 리스트로 만들기
        list2.append(list(map(int, list(remain))))
    
    # 이진수 돌면서 벽 표시하기 
    for i in range(n):
        for j in range(n):
            if list1[i][j] == 1 or list2[i][j]==1:
                arr[i][j] = 1
                
    # 정답 배열 만들기
    answer = []
    for i in range(n):
        string = ""
        for j in arr[i]: 
            if j == 1:
                string += "#"
            else:
                string += " "
        answer.append(string)
    return answer

# 테스트 1 〉	통과 (0.17ms, 10.4MB)
# 테스트 2 〉	통과 (0.44ms, 10.4MB)
# 테스트 3 〉	통과 (0.06ms, 10.4MB)
# 테스트 4 〉	통과 (0.18ms, 10.4MB)
# 테스트 5 〉	통과 (0.11ms, 10.4MB)
# 테스트 6 〉	통과 (0.25ms, 10.4MB)
# 테스트 7 〉	통과 (0.10ms, 10.4MB)
# 테스트 8 〉	통과 (0.08ms, 10.4MB)


#2차시도
def solution(n, arr1, arr2):
    arr = [[0]* n for _ in range(n)]
    list1 = []
    list2 = []
    for i in range(n):
        remain1 = ""
        remain2 = ""
        num1 = arr1[i]
        num2 = arr2[i]
        # 이진수 구하기
        for _ in range(n):
            remain1 = str(num1 % 2) + remain1
            num1 //= 2
        # string을 리스트로 만들기
        list1.append(list(map(int, list(remain1))))
        # 이진수 구하기
        for _ in range(n):
            remain2 = str(num2 % 2) + remain2
            num2 //= 2
        # string을 리스트로 만들기
        list2.append(list(map(int, list(remain2))))
        
    # 이진수 돌면서 벽 표시하기 
    for i in range(n):
        for j in range(n):
            if list1[i][j] == 1 or list2[i][j]==1:
                arr[i][j] = 1
                
    # 정답 배열 만들기
    answer = []
    for i in range(n):
        string = ""
        for j in arr[i]: 
            if j == 1:
                string += "#"
            else:
                string += " "
        answer.append(string)
    return answer

# 테스트 1 〉	통과 (0.17ms, 10.4MB)
# 테스트 2 〉	통과 (0.45ms, 10.4MB)
# 테스트 3 〉	통과 (0.05ms, 10.4MB)
# 테스트 4 〉	통과 (0.21ms, 10.4MB)
# 테스트 5 〉	통과 (0.12ms, 10.4MB)
# 테스트 6 〉	통과 (0.26ms, 10.4MB)
# 테스트 7 〉	통과 (0.09ms, 10.5MB)
# 테스트 8 〉	통과 (0.08ms, 10.4MB)