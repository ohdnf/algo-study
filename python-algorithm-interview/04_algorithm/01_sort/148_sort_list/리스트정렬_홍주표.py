# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        curr = head
        if curr is None:
            return curr

        mem = None
        max_val = float('-inf')
        while curr.next:
            if mem == head:
                break

            if curr.val > curr.next.val:
                curr.val, curr.next.val = curr.next.val, curr.val
            max_val = max(max_val, curr.val, curr.next.val)
            curr = curr.next
            
            if curr.next is None or curr == mem:
                if curr.val == max_val:
                    mem = curr
                    curr = head

        return head
