class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #problem def: indices of the two numbers such that they add up to target.
        self.n = len(nums)
        check = {}
        for i in range(self.n):
            if (target - nums[i]) in check:
                return [i, check[target - nums[i]]]
            
            else:
                check[nums[i]] = i
                