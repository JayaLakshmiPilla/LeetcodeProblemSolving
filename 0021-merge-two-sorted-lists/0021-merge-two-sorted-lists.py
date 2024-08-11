# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ansList = ListNode(-1)
        temp1 = list1 
        temp2 = list2 
        ret = ansList 
        while (temp1 or temp2) :
            if(temp1 and temp2):
                if temp1.val < temp2.val :
                    ansList.next =ListNode(temp1.val)
                    temp1 = temp1.next  
                else :
                    ansList.next = ListNode(temp2.val)
                    temp2 = temp2.next  
            elif temp1 :
                ansList.next = ListNode(temp1.val)
                temp1 = temp1.next 
            elif temp2 :
                ansList.next = ListNode(temp2.val)
                temp2 = temp2.next 
            ansList = ansList.next
        return ret.next   

                
