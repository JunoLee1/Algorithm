# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        count = 0
        node = head #traverse 
        while node:
            if node.val in nums: # if node.val is in nums
                count+=1 # connect the node
                while node and node.val in nums:
                    node = node.next
            else :node = node.next
        return count