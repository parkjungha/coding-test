# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # Run 5.7% (1147 ms) Mem 17.91% (20.5 MB)
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        li = []
        while head:
            if head in li: 
                return True
            else:
                li.append(head)

            head = head.next

        return False


# fast 가 slow를 따라잡아서 같아지면 circular linked list
# fast 가 None이 되면 not circular linked list

class Solution:
    # Run 40.87% (68 ms) Mem 34.24% (20.3 MB)
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next # slow는 한칸씩
            fast = fast.next.next # fast는 두칸씩
            if slow == fast: return True # slow와 fast가 같아지면 
        return False