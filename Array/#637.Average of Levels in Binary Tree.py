# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        level = []
        res = []
        if root is None:
            return 0
        
        level.append(root) ##starting point
        while level:
            curr = level[0]
            level.pop()
            
            if curr.left:
                level.append(curr.left)
                
            if curr.right :
                level.append(curr.right)
                
            res.append(sum(level)/ len(level))
        return res
                
                
                
    
            
            
            
            
            
            
            