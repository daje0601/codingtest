# leetcode 206. 역순 연결 리스트

# <solution1 - 최초풀이>
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        node = head
        
        answer = []
        while node:
                
            answer.append(node.val)
            node = node.next
        
        # 다시 링크드 리스트로 변경하여 제출 답안 형식으로 변경한다. 
        def lst2link(merge_list):
            cur = dummy = ListNode(0)
            for e in merge_list:
                cur.next = ListNode(e)
                cur = cur.next
            return dummy.next
        
        return lst2link(answer[::-1])

# <solution2>
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        node, prev = head, None
        
        # while node는 while nod is not None: 이라는 뜻을 가지고 있습니다. 
        while node:
            # 일단, 들어온 노드를 새로운 임시변수에 넣어줍니다. 
            temp = node 
            # 노드를 따라갈 수 있도록 node를 next으로 업데이트 합니다. 
            node = node.next 
            # temp의 next를 prev로 연결하여주고, 
            temp.next = prev
            # prev를 temp로 업데이트 합니다. 
            prev = temp 
        
        # 시작 노드만 넣어주면 쭉 출력되게 문제가 제작되어 있어서 
        # prev만 넣어주면 됩니다. 
        return prev

# <solution3>
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    
    	node, prev = head, None
        
        # solution1을 더 간결하게 적어놓은 코드라고 생각하면 된다. 
        # 중복할당의 개념이 익숙지 않는 분들은 이것을 하나하나 풀어보면 이해가 빠르게 되실 겁니다.
        while node:
            next, node.next = node.next, prev
            node, prev = next, node 
        
        return prev
