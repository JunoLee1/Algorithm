"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        Q = []
        res = []
        Q.append(root)
        
        while Q:
            level = len(Q)
            for i in range(level):
                curr = Q[0]
                Q.pop(0)
                
                if curr.children is not None:
                    Q.append(curr.children)
            res.append(curr.val)
        return res
                
        