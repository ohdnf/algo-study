# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        min_heap = [-999]

        # insert
        now = head
        while now:
            number = now.val
            min_heap.append(number)
            index = len(min_heap)-1
            while index != 1:
                parent = index // 2
                if min_heap[index] >= min_heap[parent]:
                    break
                min_heap[index], min_heap[parent] = min_heap[parent], min_heap[index]
                index = parent
            now = now.next
        sorted_list = []
        # head = None
        now = None
        # delete
        while len(min_heap) != 1:
            min_number = min_heap[1]
            if not now:
                head = ListNode(min_number)
                now = head
            else:
                now.next = ListNode(min_number)
                now = now.next
            if len(min_heap) == 2:
                break
            min_heap[1] = min_heap.pop()
            index = 1
            while True:
                min_index = index
                child1, child2 = index*2, index*2+1
                if child1 < len(min_heap) and min_heap[child1] < min_heap[min_index]:
                    min_index = child1
                if child2 < len(min_heap) and min_heap[child2] < min_heap[min_index]:
                    min_index = child2
                if min_index == index:
                    break
                min_heap[index], min_heap[min_index] = min_heap[min_index], min_heap[index]
                index = min_index
        # return sorted_list
        return head
#Runtime: 720 ms, faster than 7.18% of Python3 online submissions for Sort List.
#Memory Usage: 38.1 MB, less than 11.21% of Python3 online submissions for Sort List.