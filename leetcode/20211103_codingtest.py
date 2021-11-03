# 297. Serialize and Deserialize Binary Tree
# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/submissions/

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        queue = collections.deque([root])
        
        result = ["#"] 
        while queue:
            node = queue.popleft()
            
            if node is not None:
                queue.append(node.left)
                queue.append(node.right)
                result.append(str(node.val))
            else:
                result.append("#")
        
        return " ".join(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "# #":
            return None
        
        nodes = data.split(" ")
        
        root = TreeNode(nodes[1])
        queue = collections.deque([root])
        index = 2
        while queue:
            node = queue.popleft()
            
            if nodes[index] is not "#":
                node.left = TreeNode(int(nodes[index]))
                queue.append(node.left)
            index += 1 
            
            if nodes[index] is not "#":
                node.right = TreeNode(int(nodes[index]))
                queue.append(node.right)
            index += 1 
        
        return root
      

# 110. Balanced Binary Tree
# https://leetcode.com/problems/balanced-binary-tree/
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(root):
            if not root: 
                return 0 
        
            left = check(root.left)
            right = check(root.right)

            if left == -1 or right == -1 or abs(left-right) > 1 :
                return -1 
            return max(left, right) + 1
        return check(root) != -1 
