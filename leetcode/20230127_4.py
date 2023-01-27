# link : https://leetcode.com/problems/palindrome-linked-list/solutions/?q=python&orderBy=most_votes

# solution1
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        lst = [] 
        while head :
            lst.append(head.val)
            head = head.next
        
        if lst == lst[::-1]:
            return True
          
# solution2 
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        lst = [] 
        while head :
            lst.append(head.val)
            head = head.next
        
        while len(lst) > 1 : 
            if lst.pop(0) != lst.pop():
                return False 
        return True

# solution3
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        lst = collections.deque()
        while head :
            lst.append(head.val)
            head = head.next
        
        while len(lst) > 1 : 
            if lst.popleft() != lst.pop():
                return False 
        return True
         
