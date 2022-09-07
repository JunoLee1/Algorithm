# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = []
        res = []
      
        if not root:
            return 0
        
        q.append(root.val) ##starting point
        while root:
            curr = q[0]
            q.pop(0)
            sum1 = sum(q)/2 # the average 
            res.append(sum1)
        return res
            
            
            
            
            
            
            