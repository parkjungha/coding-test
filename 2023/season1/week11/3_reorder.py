# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # Run 66.34% (90ms) Mem 7.24% (26.1MB)
    def reorderList(self, head: Optional[ListNode]) -> None:
        array = []
        curr = head
        while curr:
            array.append(curr)
            curr = curr.next
        
        left = 0
        right = len(array) - 1
        last = head

        while left < right:
            array[left].next = array[right]
            left += 1

            if left == right: 
                break

            array[right].next = array[left]
            right -= 1

        array[left].next = None