# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        ptr = head
        size = 0
        while ptr:
            ptr = ptr.next
            size += 1
        
        idx = size - n
        ptr = head

        if idx == 0:
            return head.next

        for i in range(idx-1):
            ptr = ptr.next

        ptr.next = ptr.next.next
        return head
        
        
