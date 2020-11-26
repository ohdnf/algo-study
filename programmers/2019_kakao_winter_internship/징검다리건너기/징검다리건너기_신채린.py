def solution(stones, k):
    count = 0
    step = 0
    while True:
        for i in range(len(stones)):
            if stones[i] != 0:
                stones[i] -= 1
            else:
                step += 1
                if step > k:
                    break
        count +=1 
        step = 0
    return count