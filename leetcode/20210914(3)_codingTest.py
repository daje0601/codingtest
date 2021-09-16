# leetcode 21. merge_list 

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # 일단 두개의 링크드 리스트를 일반 리스트로 나는 변경을 해주었다. 
        list1, list2 = [], []
        
        node = l1
        while node != None:
            list1.append(node.val)
            node = node.next
    
        node2 = l2
        while node2 != None:
            list2.append(node2.val)
            node2 = node2.next
        
        # 일반 리스트로 변경된 두개의 리스트를 더하고 정렬을 해준 후 
        merge_list = sorted(list1+list2)
        
        # 다시 링크드 리스트로 변경하여 제출 답안 형식으로 변경한다. 
        def lst2link(merge_list):
            cur = dummy = ListNode(0)
            for e in merge_list:
                cur.next = ListNode(e)
                cur = cur.next
            return dummy.next
        
        return lst2link(merge_list)
      
## ------------------------------------------------------

# solution1 - discussion 참조 
class Solution:
    def mergeTwoLists(self, a, b):
        if a and b:
            if a.val > b.val:
                a, b = b, a
            a.next = self.mergeTwoLists(a.next, b)
        return a or b
  
## ------------------------------------------------------

# solution2 - discussion 참조 
class Solution:
    def mergeTwoLists(self, a, b):
        # a가 b보다 큰 경우 
        # not a라는 것은 링크드 리스트가 None이냐고 묻는 것이다. 
        # 링크드 리스트 맨 마지막에는 None이 들어있기 때문에 a가 끝이라면 a를 맨 뒤로 보내는 작업 필요하다. 
        # b and a.val > b.val는 b가 남아 있는 상황이고 그게 a가 더 크다면 a랑 b랑 위치를 바꿔야 한다. 
        if not a or b and a.val > b.val:
            a, b = b, a
        
        # a가 b보다 작은 경우 
        if a:
            a.next = self.mergeTwoLists(a.next, b)
        return a
