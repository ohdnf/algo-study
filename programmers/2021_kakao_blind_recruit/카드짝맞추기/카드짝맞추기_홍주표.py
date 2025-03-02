from collections import deque, defaultdict
from itertools import permutations


def bfs(cards, start, finish):
    visited = [[False for _ in range(4)] for _ in range(4)]
    visited[start[0]][start[1]] = True
    queue = deque([(start[0], start[1], 0)])
    while queue:
        cr, cc, moved = queue.popleft()
        # finish?
        if cr == finish[0] and cc == finish[1]:
            return moved + 1  # count flipping card
        # search
        for dr, dc in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            # move
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < 4 and 0 <= nc < 4 and not visited[nr][nc]:
                visited[nr][nc] = True
                queue.append((nr, nc, moved + 1))
                # cursor cannot go beyond the card
                if cards[nr][nc]:
                    continue
            # ctrl + move
            while True:
                nr += dr
                nc += dc
                if not (0 <= nr < 4 and 0 <= nc < 4):
                    nr -= dr
                    nc -= dc
                    break
                if cards[nr][nc]:
                    break

            if 0 <= nr < 4 and 0 <= nc < 4 and not visited[nr][nc]:
                visited[nr][nc] = True
                queue.append((nr, nc, moved + 1))


def solution(board, r, c):
    card_number = set()  # distinct card numbers
    # group coordinates of the cards by number
    card_location = defaultdict(list)
    for row in range(4):
        for col in range(4):
            if board[row][col]:
                card_number.add(board[row][col])
                card_location[board[row][col]].append((row, col))
    # list all routes
    candidates = []
    for numbers in permutations(card_number):
        routes = deque()
        for num in numbers:
            first, second = card_location[num]
            if routes:
                for _ in range(len(routes)):
                    route = routes.popleft()
                    routes.append(route + [first, second])
                    routes.append(route + [second, first])
            else:
                routes.append([first, second])
                routes.append([second, first])
        candidates.extend(list(routes))
    # search the shortest route
    answer = float('inf')
    for candidate in candidates:
        cards = [[True if board[row][col]
                  else False for col in range(4)] for row in range(4)]
        move = 0
        cursor = (r, c)  # cursor location
        for card in candidate:
            # find the shortest route from the card before to the next card
            move += bfs(cards, cursor, card)
            cards[card[0]][card[1]] = False
            cursor = card
        answer = min(answer, move)
    return answer


if __name__ == '__main__':
    print(solution([[1, 0, 0, 3], [2, 0, 0, 0],
          [0, 0, 0, 2], [3, 0, 1, 0]], 1, 0), 14)
    print(solution([[3, 0, 0, 2], [0, 0, 1, 0],
          [0, 1, 0, 0], [2, 0, 0, 3]], 0, 1), 16)
    print(solution([[1, 0, 0, 0], [0, 0, 0, 0],
          [0, 0, 0, 0], [0, 0, 0, 1]], 0, 0), 4)
