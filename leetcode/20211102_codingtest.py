# 226. Invert Binary Tree
# 링크 : https://leetcode.com/problems/invert-binary-tree/
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if root :
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            return root 
        
        return None
      
      
# 617. Merge Two Binary Trees
# 링크 : https://leetcode.com/problems/merge-two-binary-trees/
class Solution:
    def mergeTrees(self, t1: Optional[TreeNode], t2: Optional[TreeNode]) -> Optional[TreeNode]:
        if t1 and t2:
            node = TreeNode(t1.val + t2.val)
            node.left = self.mergeTrees(t1.left, t2.left)
            node.right = self.mergeTrees(t1.right, t2.right)
            return node 
        else:
            return t1 or t2
