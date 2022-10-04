class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        self.helper(nums, [], ans)
        return ans
    def helper(self, nums, temp, ans):
        if len(nums) == 0:
            ans.append(temp)
            
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            self.helper(nums[:i] + nums[i + 1:], temp + [nums[i]], ans)
                