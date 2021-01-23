# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        parent = ListNode(0)
        cur = parent
        while head:
            # 삽입할 head.val값을 기존의 값과 왼쪽부터 비교하여 위치를 결정한다.
            while cur.next and cur.next.val < head.val:
                cur = cur.next
            # 결정된 위치(cur.next)에 head를 넣어준다(값은 원래값, next는 cur.next가 가리키던 주소) => head = head.next로 head는 갱신  
            cur.next, head.next, head = \
            head,     cur.next,  head.next
            # cur의 위치 복귀
            cur = parent
        return parent.next
# Runtime: 1996 ms, faster than 26.17% of Python3 online submissions for Insertion Sort List.
# Memory Usage: 16.3 MB, less than 62.81% of Python3 online submissions for Insertion Sort List.
# class Solution:
#     def insertionSortList(self, head: ListNode) -> ListNode:
#         cur = parent = ListNode(0)
#         while head:
#             while cur.next and cur.next.val < head.val:
#                 cur = cur.next
#             cur.next, head.next, head = head, cur.next, head.next
            
#             if head and cur.val > head.val:
#                 cur = parent
#         return parent.next
# Runtime: 172 ms, faster than 89.14% of Python3 online submissions for Insertion Sort List.
# Memory Usage: 16.3 MB, less than 62.81% of Python3 online submissions for Insertion Sort List.