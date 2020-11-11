def solution(n, arr1, arr2):
    # 벽(#) => arr = arr1 || arr2
    arr = []
    # default는 " "로 놓고, 해당되는 곳만 "#"로 변환
    for idx in range(n):
        num1 = arr1[idx]
        num2 = arr2[idx]
        temp = [" "] * n
        for i in range(1, n+1):
            if num1 % 2 or num2 % 2:
                temp[-i] = "#"
            num1, num2 = num1 // 2, num2 // 2
            # 둘다 0이여서 계속 계산할 필요 X
            if not num1 and not num2:
                break
        arr.append(temp)
    # 공백만을 포함한 스트링을 합치기 위해서, 일일히 구현
    answer = []
    for a in arr:
        st = ""
        for s in a:
            st += s
        answer.append(st) 
    return answer