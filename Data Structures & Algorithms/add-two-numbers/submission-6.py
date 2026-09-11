class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = l1
        cur1, cur2 = l1, l2
        prev = None
        carry = 0

        while cur1 or cur2:
            # If l1 runs out, attach the rest of l2
            if not cur1:
                prev.next = cur2
                cur1 = cur2
                cur2 = None

            total = cur1.val + (cur2.val if cur2 else 0) + carry

            cur1.val = total % 10
            carry = total // 10

            prev = cur1
            cur1 = cur1.next

            if cur2:
                cur2 = cur2.next

        if carry:
            prev.next = ListNode(carry)

        return head