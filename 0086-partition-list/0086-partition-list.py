# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # Create two dummy nodes to start the before and after lists
        before_head = ListNode(0)
        after_head = ListNode(0)
        
        # Pointers to the current last nodes of before and after lists
        before = before_head
        after = after_head
        
        # Traverse the original list
        while head:
            if head.val < x:
                before.next = head
                before = before.next
            else:
                after.next = head
                after = after.next
            head = head.next
        
        # Make sure the last node of 'after' list points to None
        after.next = None
        # Connect the before list with the after list
        before.next = after_head.next
        
        return before_head.next
