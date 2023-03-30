# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        res = ""
        while head:
            res += str(head.val)
            head = head.next
        return res == res[::-1]

    def isPalindrome(self, head: Optional[ListNode]) -> bool:      
        if not head or not head.next: # 비어있거나 하나뿐이면
            return True

        slow = fast = head
        rev = None

        # reverse left half of the list while searching
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        
        if fast:
            slow = slow.next
        
        while rev:
            if rev.val != slow.val:
                return False
            rev, slow = rev.next, slow.next
        
        return True