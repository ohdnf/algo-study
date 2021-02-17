# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        curr = root = ListNode(None)
        while head:
            while curr.next and curr.next.val < head.val:
                curr = curr.next
            curr.next, head.next, head = head, curr.next, head.next
            
            curr = root
            
        return root.next


"""
Runtime: 1956 ms, faster than 33.07% of Python3 online submissions for Insertion Sort List.
Memory Usage: 16.3 MB, less than 87.54% of Python3 online submissions for Insertion Sort List.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        curr = root = ListNode()
        while head:
            while curr.next and curr.next.val < head.val:
                curr = curr.next
            curr.next, head.next, head = head, curr.next, head.next
            
            if head and curr.val > head.val:
                curr = root
            
        return root.next


"""
Runtime: 172 ms, faster than 87.90% of Python3 online submissions for Insertion Sort List.
Memory Usage: 16.4 MB, less than 23.12% of Python3 online submissions for Insertion Sort List.
"""