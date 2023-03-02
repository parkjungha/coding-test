# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Recursion # 

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        for _ in range(k):
            if not curr: return head
            curr = curr.next
        
        # Reverse each group
        prev = None
        curr = head
        for _ in range(k):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        # 한번 reverse하면 head가 tail이 되고, curr이 해당 group의 next pointer를 가르킴
        head.next = self.reverseKGroup(curr,k)
        return prev

#######################################################################################

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = jump = ListNode(0)
        dummy.next = l = r = head
        
        while True:
            count = 0
            while r and count < k:   # r을 k만큼의 범위까지 이동시킴
                r = r.next
                count += 1

            if count == k:  # k에 다다르면 l부터 r까지의 group내부를 reverse 
                prev, curr = r, l # l(curr)부터 r(prev)까지
                for _ in range(k):
                    curr.next, curr, prev = prev, curr.next, curr  # standard reversing
                
                # reverse하고 나면 prev가 head로, curr가 tail에서 next point를 가리킴
                # 이전 그룹의 next와 현재의 맨앞을 연결시켜줌
                jump.next, jump, l = prev, l, r  # connect two k-groups
            else:
                return dummy.next