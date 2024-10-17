# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()
        curr = dummy
        while l1 != None or l2 != None:
            if l1 != None:
                carry += l1.val
                l1 = l1.next
            if l2 != None:
                carry += l2.val
                l2 = l2.next
            curr.next = ListNode(carry%10)
            carry = 1 if carry>=10 else 0
            curr = curr.next    
        if carry != 0:        
            curr.next= ListNode(carry)
        return dummy.next
