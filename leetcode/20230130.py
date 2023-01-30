class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if (not l1) or (l2 and l1.val > l2.val):
            l1, l2 = l2, l1 
        if l1 :
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1
 
# 처음에는 이 코드가 이해가 안됐는데, 
# l1.val > l2.val이라고 하면 아에 링크드 리스트를 변경해버렸음
