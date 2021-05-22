'''
동작
- 일반
- ctrl

보드 4x4
카드 최대 6*2
'''
from collections import defaultdict, deque
from itertools import permutations

def go(board, cards, start, path):
    # path는 1칸씩 짧아짐
    
    if not path: # 종료 조건
        return 0
    
    # 각 단계별 한 쌍의 카드중 어느쪽을 먼저가는지 2가지 경우 존재
    
    dst1, dst2 = cards[path[-1]] # 목적지
    
    return min(
        # 케이스1
        dist(board, start, dst1, path) + dist(board, dst1, dst2, path) + go(board, cards, dst2, path[:-1]),
        # 케이스2
        dist(board, start, dst2, path) + dist(board, dst2, dst1, path) + go(board, cards, dst1, path[:-1])
    )
    # 케이스2
    
def dist(board, a, b, path):
    r, c = a
    dst_r, dst_c = b
    
    path_dict = {i:1 for i in path}
    
    q = deque([(r,c)])
    v = defaultdict(list) # 좌표 방문 여부
    v[(r,c)] = 1
    
    cnt = -1 # 움직인 횟수
    while q:
        cnt += 1
        for _ in range(len(q)):
            r, c = q.popleft()
            
            # 목적지 여부 확인
            if r == dst_r and c == dst_c:
                return cnt
            
            for dr, dc in ((0,1), (0,-1), (1,0), (-1,0)): # 4방향

                # 1칸 조작
                nr, nc = r + dr, c + dc
                if 0 <= nr < 4 and 0 <= nc < 4 and (nr,nc) not in v:
                    q.append((nr,nc))
                    v[(nr,nc)] = 1
                
                # ctrl 조작
                for i in range(1, 3+1):
                    nr, nc = r + dr*i, c + dc*i
                    
                    # 경계 조건
                    if 0 <= nr < 4 and 0 <= nc < 4:
                        
                        # 카드 있음 => 종료 (nr, nc 보존)
                        if board[nr][nc] in path_dict:
                            break
                            
                    else:
                        
                        # 경계 초과 => nr, nc 변경
                        nr, nc = r + dr*(i-1), c + dc*(i-1) # i-1은 0~2까지 가능
                        break
                if (nr, nc) not in v:
                    q.append((nr,nc))
                    v[(nr,nc)] = 1
                        
    
def solution(board, r, c):
    start = (r,c)
    cards = defaultdict(list) # [(r1,c1), (r2,c2)] 
    for r in range(4):
        for c in range(4):
            if board[r][c]:
                cards[board[r][c]].append((r,c))
    answer = float('inf')
    for path in permutations(cards.keys()):
        answer = min(answer, go(board, cards, start, path))
                
    return answer + 2*len(cards.keys())
'''
테스트 1 〉	통과 (6.01ms, 10.3MB)
테스트 2 〉	통과 (5.89ms, 10.4MB)
테스트 3 〉	통과 (6.00ms, 10.3MB)
테스트 4 〉	통과 (4.93ms, 10.4MB)
테스트 5 〉	통과 (36.15ms, 10.3MB)
테스트 6 〉	통과 (36.24ms, 10.3MB)
테스트 7 〉	통과 (40.01ms, 10.4MB)
테스트 8 〉	통과 (38.64ms, 10.3MB)
테스트 9 〉	통과 (403.45ms, 10.2MB)
테스트 10 〉통과 (422.87ms, 10.4MB)
테스트 11 〉통과 (390.65ms, 10.3MB)
테스트 12 〉통과 (414.71ms, 10.4MB)
테스트 13 〉통과 (4916.36ms, 10.3MB)
테스트 14 〉통과 (5868.71ms, 10.4MB)
테스트 15 〉통과 (4247.19ms, 10.3MB)
테스트 16 〉통과 (5030.83ms, 10.5MB)
테스트 17 〉통과 (0.28ms, 10.3MB)
테스트 18 〉통과 (0.09ms, 10.4MB)
테스트 19 〉통과 (1.30ms, 10.3MB)
테스트 20 〉통과 (1.10ms, 10.5MB)
테스트 21 〉통과 (32.85ms, 10.3MB)
테스트 22 〉통과 (6150.29ms, 10.3MB)
테스트 23 〉통과 (5562.50ms, 10.4MB)
테스트 24 〉통과 (43.14ms, 10.3MB)
테스트 25 〉통과 (5678.57ms, 10.3MB)
테스트 26 〉통과 (45.20ms, 10.3MB)
테스트 27 〉통과 (42.90ms, 10.4MB)
테스트 28 〉통과 (6.45ms, 10.3MB)
테스트 29 〉통과 (5.43ms, 10.5MB)
테스트 30 〉통과 (5.35ms, 10.4MB)
'''