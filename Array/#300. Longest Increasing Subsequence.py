class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
       # prob def : return the length of the longest strictly increasing subsequence.
       # f(i, j) = the length of the longest strictly increasing subsequence from i to j
        n = len(nums)
        dp = [1] * n
        
        for i in range(n): #  
            for j in range(i): # 0 
                if nums[i] > nums[j]: #뒤의 nums가  앞의 nums보다 클때
                    dp[i] = max(dp[j] + 1, dp[i]) #
        return max(dp)
        