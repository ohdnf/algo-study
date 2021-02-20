def solution(files):
    sortedFiles = []
    for file in files:
        head_idx, number_idx = None, None
        for i in range(len(file)):
            if file[i].isnumeric():
                break 
            else:
                head_idx = i
        for i in range(head_idx + 1, len(file)):
            if file[i].isnumeric(): 
                number_idx = i
            else:
                break 
        sortedFiles.append([file[:head_idx+1], file[head_idx+1:number_idx+1], file[number_idx+1:]])
    answer = sorted(sortedFiles, key=lambda x: (x[0].lower(), int(x[1])))
                        
    return ["".join(i) for i in answer]

'''
테스트 1 〉	통과 (0.05ms, 10.4MB)
테스트 2 〉	통과 (0.05ms, 10.5MB)
테스트 3 〉	통과 (3.19ms, 11MB)
테스트 4 〉	통과 (3.22ms, 10.8MB)
테스트 5 〉	통과 (3.15ms, 11MB)
테스트 6 〉	통과 (3.22ms, 10.9MB)
테스트 7 〉	통과 (3.08ms, 10.9MB)
테스트 8 〉	통과 (4.40ms, 10.7MB)
테스트 9 〉	통과 (2.84ms, 10.9MB)
테스트 10 〉	통과 (2.98ms, 10.7MB)
테스트 11 〉	통과 (2.94ms, 10.6MB)
테스트 12 〉	통과 (2.85ms, 10.9MB)
테스트 13 〉	통과 (2.75ms, 10.8MB)
테스트 14 〉	통과 (2.96ms, 11.2MB)
테스트 15 〉	통과 (2.82ms, 11.2MB)
테스트 16 〉	통과 (3.01ms, 10.9MB)
테스트 17 〉	통과 (2.56ms, 10.8MB)
테스트 18 〉	통과 (2.52ms, 10.8MB)
테스트 19 〉	통과 (2.93ms, 10.8MB)
테스트 20 〉	통과 (2.67ms, 10.8MB)
'''


# 망한코드 - 55점 
# def solution(files):
#     sortedFiles = []
#     for file in files:
#         idx = 0
#         head, number, tail = "", "", ""
#         current = "head"
#         while idx < len(file):
#             if current == "head" and file[idx].isnumeric() == False:
#                 head += file[idx]
#             elif (current == "head" or current == "number") and file[idx].isnumeric():
#                 current = "number"
#                 number += file[idx]
#             else:
#                 current == "tail"
#                 tail += file[idx]
#             idx += 1
#         sortedFiles.append([head, number, tail])
#     answer = sorted(sortedFiles, key=lambda x: (x[0].lower(), int(x[1])))
                        
#     return ["".join(i) for i in answer]