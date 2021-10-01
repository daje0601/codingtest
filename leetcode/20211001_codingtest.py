# 23. Merge k Sorted Lists
# 링크 : https://leetcode.com/problems/merge-k-sorted-lists/

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        lst = []
        for i in range(len(lists)):
            node = lists[i] 
            while node :
                lst.append(node.val)
                node = node.next 
        lst = sorted(lst)
        
        def lst2link(lst):
            cur = dummy = ListNode(0)
            for e in lst:
                cur.next = ListNode(e)
                cur = cur.next
            return dummy.next
        
        if lst is None:
            return []
        else:
            return lst2link(lst)

          
  ---
  
# 706. Design HashMap
# 링크 : https://leetcode.com/problems/design-hashmap/submissions/
class MyHashMap:

    def __init__(self):
        self.hash = {}

    def put(self, key: int, value: int) -> None:
        self.hash[key] = value        

    def get(self, key: int) -> int:
        if key in self.hash:
            return self.hash[key]
        else:
            return -1

    def remove(self, key: int) -> None:
        if key in self.hash:
            del(self.hash[key])
