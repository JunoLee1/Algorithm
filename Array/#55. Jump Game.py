class Solution:
    def canJump(self, nums: List[int]) -> bool:
        j = 0
        
        for jump, k in enumerate(nums):
            if jump > j :
                return False
            j = max(j, jump + k)
            
        return True
            
