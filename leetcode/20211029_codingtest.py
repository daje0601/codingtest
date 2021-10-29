# 543. Diameter of Binary Tree
# 링크 : https://leetcode.com/problems/diameter-of-binary-tree/submissions/
class Solution:
    result = 0 
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            if node is None:
                return -1
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            self.result = max(self.result, left+right+2)
            return max(left, right)+1
        dfs(root)
        return self.result 
      
      
# 687. Longest Univalue Path
# 링크 : https://leetcode.com/problems/maximum-depth-of-binary-tree/
class Solution:
    result = 0 
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node is None:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            if node.left and node.left.val==node.val:
                left+=1
            else:
                left = 0 
            if node.right and node.right.val==node.val:
                right += 1
            else:
                right = 0 
            
            self.result = max(self.result, left+right)
            return max(left, right)
        dfs(root)
        
        return self.result 
