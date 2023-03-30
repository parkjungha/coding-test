# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  # One pointer. 첫번째 iteration으로 linked list 길이 파악. 제거해야할 idx 계산해서 앞에서부터 iteration돌면서 도착하면 삭제함
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
      curr, leng = head, 0 
      while curr:
        curr = curr.next
        leng += 1
      if leng == n: return head.next
      curr = head
      for i in range(leng - n - 1):
        curr = curr.next
      curr.next = curr.next.next
      
      return head
  # Two pointers. Fast and Slow pointer with gap of n!
    def removeNthFronEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
      fast, slow = head, head
      for i in range(n):
        fast = fast.next

      if not fast: return head.next 

      while fast.next:
        slow = slow.next
        fast = fast.next
      
      slow.next = slow.next.next

      return head