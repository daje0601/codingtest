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
 
#soution4 런너를 사용한 방법 
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # 먼저, slow와 fast를 head정의한다. 
        # fast는 두칸씩 이동하고 slow는 한칸씩 이동할 것이다. 
        slow = fast = head 
        # 펠런드롭을 확인할 rev를 정의한다. 
        # rev는 딱 절반에 해당하는 노드들만 역으로 저장할 것이다. 
        rev = None 
        
        # fast가 있고, fast.next가 있을 때까지 rev를 만들게 된다. 
        while fast and fast.next :
            fast = fast.next.next 
            slow, rev, rev.next = slow.next, slow, rev
        
        # 입력받은 연결리스트가 홀수인 경우를 대비해서 이 과정을 거치게 된다. 
        # 짝수인경우 fast는 None으로 지정이 되어 있을 것이고, 
        # 홀수인경우 한 가운데 노드에 걸치기 때문에 slow가 한칸 더 앞으로 나아가야한다. 
        if fast : 
            slow = slow.next 
        
        # 이제 펠렌드롬을 확인할 차례이다 값을 비교하면 되고 
        # 모두 진행되면, slow, rev 모두 None이 지정될 것이다. 
        # None은 기본적으로 False이기 때문에 not rev or not val 로 return 값을 주면 된다. 
        while rev and rev.val == slow.val :
            rev, slow = rev.next, slow.next 
            
        return not rev
