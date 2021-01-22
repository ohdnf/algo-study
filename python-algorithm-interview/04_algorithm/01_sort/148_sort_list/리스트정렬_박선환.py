# 기존 규정된 Linked List를 활용해서 풀어보려고 했으나 결국 생각이 나지 않았다리...
# 책 풀이를 참고해 따라 풀어봄!
# 런너 기법을 활용해서 분할하는 점이 신기했음!

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1 or l2 # l1(val이 가장 작은 값의 노드가 head) 우선 출력
    
    def sortList(self, head: ListNode) -> ListNode:
        if not (head and head.next): # None이거나 리프노드 일 때 return
            return head

        # 러너 기법
        half, slow, fast = None, head, head
        while fast and fast.next:
            half, slow, fast = slow, slow.next, fast.next.next
            # 결국 slow가 right ListNode가 됨.
        half.next = None # head ListNode의 half 이후를 끊어주기 => head를 Left ListNode로
        
        # 재귀!
        l1 = self.sortList(head)
        l2 = self.sortList(slow)
        
        return self.mergeTwoLists(l1, l2)

'''
Runtime: 564 ms, faster than 21.17% of Python3 online submissions for Sort List.
Memory Usage: 51 MB, less than 5.25% of Python3 online submissions for Sort List.
'''