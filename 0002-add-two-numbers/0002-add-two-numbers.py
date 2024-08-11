# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        carry = 0
        ans = ListNode()
        res = ans
        while (l1 != None or l2 != None) :
            sum = carry 
            if (l1 ) :
                sum= sum + l1.val            
                l1 = l1.next 
            if l2 :
                sum = sum + l2.val
                l2 = l2.next
            ans.next = ListNode(sum%10) 
            carry = sum // 10 
            ans = ans.next 
        if carry == 1 :
            ans.next = ListNode(carry) 
        return res.next
            
              

        
        