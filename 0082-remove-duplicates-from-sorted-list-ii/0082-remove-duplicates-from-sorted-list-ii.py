class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(0, head)  # Dummy node before head
        prev = dummy               # Previous distinct node
        current = head             # Pointer to traverse list

        while current:
            # Detect duplicate
            if current.next and current.val == current.next.val:
                # Skip all duplicates
                while current.next and current.val == current.next.val:
                    current = current.next
                prev.next = current.next  # Remove all duplicates
            else:
                prev = prev.next  # No duplicate; move prev
            current = current.next

        return dummy.next
