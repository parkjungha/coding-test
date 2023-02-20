
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        result = ListNode() # 첫번째 노드 
        curr = result # 포인터 역할 

        while (l1 or l2 or carry):
            l1_num = l1.val if l1 else 0
            l2_num = l2.val if l2 else 0

            sum = l1_num + l2_num + carry
            num = sum % 10 # 나머지
            carry = sum // 10 # 몫(1)

            curr.next = ListNode(num) # 1 뒤로 넘겨줌

            curr = curr.next # 다음 노드로
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return result.next
