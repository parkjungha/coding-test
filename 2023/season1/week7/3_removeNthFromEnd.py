# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
  # One pointer. 첫번째 iteration으로 linked list 길이 파악. 제거해야할 idx 계산해서 앞에서부터 iteration돌면서 도착하면 삭제함
  # Runtime 73.11% (33ms) Memory 96.89% (13.8MB)
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

  # Two pointers. Fast and Slow pointer with gap of n
  # Runtime 97.8% (26ms) Memory 96.89% (13.8MB)
    def removeNthFronEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
      fast, slow = head, head
      for i in range(n):
        fast = fast.next

      if not fast: return head.next 

      while fast.next:
        slow = slow.next
        fast = fast.next
      
      # Fast가 마지막 노드에 도착할 때, Fast와 Slow의 간격이 n만큼 있으니까 Slow는 뒤에서 n번째 노드에 도착한 것 
      slow.next = slow.next.next

      return head