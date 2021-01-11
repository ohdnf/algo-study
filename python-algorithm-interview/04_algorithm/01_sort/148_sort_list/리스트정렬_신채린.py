# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#리스트 정렬 링크드리스트 방법 
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        pre = head
        lst =[]
        while pre:
            lst.append(pre.val)
            pre = pre.next 
        lst.sort()
        
        #리스트 -> singly linked list
        pre = head
        for i in range(len(lst)):
            pre.val = lst[i]
            pre = pre.next 
        return head 
# Runtime: 160 ms, faster than 97.05% of Python3 online submissions for Sort List.
# Memory Usage: 30.2 MB, less than 63.65% of Python3 online submissions for Sort List.

# 병합정렬 방법 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        #링크드 리스트 리스트로 변경하기
        pre = head
        lst = []
        while pre:
            lst.append(pre.val)
            pre = pre.next 
        # print(lst)
        # 병합정렬
        def merge_sort(lst):
            n = len(lst)
            if n <= 1:
                return lst
            # 분할 단계 절반 나누기
            mid = n//2
            front = merge_sort(lst[:mid])
            back = merge_sort(lst[mid:])
            
            result = []
            while front and back:
                if front[0] < back[0]:
                    result.append(front.pop(0))
                else:
                    result.append(back.pop(0))
            
            #그 이후에도 각 배열이 남아있다면?
            while front:
                result.append(front.pop(0))
            while back:
                result.append(back.pop(0))
            return result 
        result = merge_sort(lst)
        #리스트를 링크드 리스트로 변경하기
        pre = head 
        for i in range(len(result)):
            pre.val = result[i]
            pre = pre.next 
        return head
        #Runtime: 668 ms, faster than 8.64% of Python3 online submissions for Sort List.
        #Memory Usage: 31.1 MB, less than 23.05% of Python3 online submissions for Sort List.