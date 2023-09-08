
# Runtime 91.69% Memory 98.52%

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merge = []
        while list1 and list2: # 둘다 값이 있을때 까지 반복
            l1, l2 = list1.val, list2.val
            if l1 > l2:
                merge.append(l2)
                list2 = list2.next
            elif l1 <= l2:
                merge.append(l1)
                list1 = list1.next

        head = result = ListNode(0)

        for i in merge:
            result.next = ListNode(i)
            result = result.next

        # 어느하나라도 남아있으면 뒤에다 붙여줌
        if list1:
            result.next = list1
        if list2:
            result.next = list2
        
        return head.next
