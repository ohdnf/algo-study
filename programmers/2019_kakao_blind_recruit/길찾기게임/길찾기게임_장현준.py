'''카카오 블라인드 2019 길찾기게임
x
- 모두 다르다.
- 좌측자식노드tree < 부모노드 < 우측자식노드tree

y
- level
- 부모노드 > 자식노드

기타
- 0 <= x,y 정수 좌표 <= 100,000
- 트리깊이 < 1,000
- 1 <= 노드 <= 10,000

'''
import sys
sys.setrecursionlimit(10**6)
from collections import deque
def create_node(info, parent_node):
    return {
        'x': info[0],
        'y': info[1],
        'index': info[2], 
        'parent': parent_node,
        'left': None,
        'right': None,
    }
def preorder(node, lst):
    if node == None:
        return
    lst.append(node['index'])
    preorder(node['left'], lst)
    preorder(node['right'], lst)
def postorder(node, lst):
    if node == None:
        return
    postorder(node['left'], lst)
    postorder(node['right'], lst)
    lst.append(node['index'])
    
def solution(nodeinfo):
    # y 기준 sort => level: 부모 / 자식노드
    nodeinfo = [(nodeinfo[i][0], nodeinfo[i][1], i+1)for i in range(len(nodeinfo))] # x,y,index
    nodeinfo = sorted(nodeinfo, key=lambda x: (-x[1], x[0]))
    
    root = create_node(nodeinfo[0], None)

    for info in nodeinfo[1:]:
        x = info[0]
        p = root
        while True:
            if x < p['x']:
                if p['left'] == None:
                    p['left'] = create_node(info, p)
                    break
                else:
                    p = p['left']
                    continue
            if x > p['x']:
                if p['right'] == None:
                    p['right'] = create_node(info, p)
                    break
                else:
                    p = p['right']
                    continue
    answer = [[], []]
    preorder(root, answer[0])
    postorder(root, answer[1])
    return answer

'''
테스트 1 〉	통과 (0.03ms, 10.3MB)
테스트 2 〉	통과 (0.06ms, 10.1MB)
테스트 3 〉	통과 (0.02ms, 10.3MB)
테스트 4 〉	통과 (0.01ms, 10.3MB)
테스트 5 〉	통과 (0.02ms, 10.3MB)
테스트 6 〉	통과 (39.30ms, 11.5MB)
테스트 7 〉	통과 (58.31ms, 11.5MB)
테스트 8 〉	통과 (36.47ms, 13.4MB)
테스트 9 〉	통과 (160.02ms, 18.4MB)
테스트 10 〉통과 (11.08ms, 11.6MB)
테스트 11 〉통과 (151.29ms, 18.4MB)
테스트 12 〉통과 (172.93ms, 18.5MB)
테스트 13 〉통과 (0.58ms, 10.3MB)
테스트 14 〉통과 (3.16ms, 11MB)
테스트 15 〉통과 (15.55ms, 14.2MB)
테스트 16 〉통과 (33.58ms, 18.2MB)
테스트 17 〉통과 (3.28ms, 11.1MB)
테스트 18 〉통과 (35.59ms, 18.2MB)
테스트 19 〉통과 (6.58ms, 11.6MB)
테스트 20 〉통과 (14.02ms, 13.7MB)
테스트 21 〉통과 (21.28ms, 15MB)
테스트 22 〉통과 (34.15ms, 18.1MB)
테스트 23 〉통과 (36.63ms, 18.2MB)
테스트 24 〉통과 (0.03ms, 10.1MB)
테스트 25 〉통과 (0.03ms, 10.3MB)
테스트 26 〉통과 (83.08ms, 12.3MB)
테스트 27 〉통과 (0.03ms, 10.3MB)
테스트 28 〉통과 (0.05ms, 10.3MB)
테스트 29 〉통과 (0.01ms, 10.2MB)
'''