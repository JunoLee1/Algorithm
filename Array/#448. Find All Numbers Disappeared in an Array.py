class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)
        
        for e in range(1, n + 1):
            if e == abs(nums[e-1]):
                -1*abs(nums[e-1])
                
        for i in range(n):
            if nums[i] > 0:
                res.append(nums[i])
        return res
      
            