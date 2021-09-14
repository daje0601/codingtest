# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        answer = []
        
        node = head 
        
        while node != None:
            answer.append(node.val)
            node = node.next
        
        if answer != answer[::-1]:
            return False
        return True
        
