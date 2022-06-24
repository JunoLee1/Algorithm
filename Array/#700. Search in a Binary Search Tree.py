# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        stack = []
        stack.append(root)
        
        while stack:
            if stack[-1].val == val:
                return stack[-1]
            
            else:
                N = stack.pop()
                if val > N.val:
                    if N.right!=None:
                        stack.append(N.right)
                else:
                    if N.left!=None:
                        stack.append(N.left)
        
        return None
            