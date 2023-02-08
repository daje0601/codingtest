# 문제 링크 : https://leetcode.com/problems/add-two-numbers/
# 문제 이름 : 2. Add Two Numbers
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        root = head = ListNode(0)

        # 더했을때 십의자리를 받을 수 있도록 캐리 변수 지정 
        carry = 0 
        
        while l1 or l2 or carry :
            sum = 0 
            if l1 : 
                sum += l1.val 
                l1 = l1.next 
            if l2 :
                sum += l2.val 
                l2 = l2.next 

            # 10으로 나누었을 때 10이 넘는 경우, carry에 전달 나머지는 val로 저장 
            carry, val = divmod(sum + carry, 10)
            head.next = ListNode(val)
            head = head.next 
        
        return root.next
