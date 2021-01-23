# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        result = ListNode(None) # 빈 ListNode 생성
        while head: # 최초의 ListNode가 다 남아있을 때까지
            c_node = ListNode(head.val) # 가장 앞의 노드 값을 가진 단일 노드
            head = head.next # head 노드리스트 업데이트
            
            tmp = result
            while True:
                if tmp.next:
                    if c_node.val < tmp.next.val: # 여기서 멈추고 삽입
                        c_node.next = tmp.next
                        tmp.next = c_node
                        break
                else: # 끝에 다다른 경우
                    tmp.next = c_node
                    break
                tmp = tmp.next # 삽입 이전, 포인터 다음으로 옮겨주기
                    
        return result.next

'''
Runtime: 1932 ms, faster than 42.51% of Python3 online submissions for Insertion Sort List.
Memory Usage: 17.4 MB, less than 6.42% of Python3 online submissions for Insertion Sort List.
'''