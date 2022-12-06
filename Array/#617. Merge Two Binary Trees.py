# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:   # merge two binary Trees 
        res = []
        if not root1:
            return 
        if not root2:
            return 
        self.dfs(root1, root2, 0, 0, res)
       
    def dfs(self,node1, node2, root1_level, root2_level, res):
        tmp = 0
        if not node1:
            return 
        if not node2:
            return 
        while node1 is not None or node2 is not None:
            if root1_level == root2_level:
                tmp = node1.val + node2.val 
                res.append(tmp)
            self.dfs(node1.left, node2.left, root1_level + 1, root2_level, res)
            self.dfs(node1.right, node2.right, root1_level, root2_level + 1, res)
        return TreeNode(res)