# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes = []
        head = point = ListNode(0)
        for l in lists:
            while l: # 모든 숫자 다 nodes 에 넣음
                nodes.append(l.val)
                l = l.next 

        nodes.sort() # 정렬
        for i in nodes:
            point.next = ListNode(i)
            point = point.next
        return head.next