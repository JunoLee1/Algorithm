class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.helper(nums, [], ans)
        return ans
    
    def helper(self, nums, temp, ans):
        if len(nums) == 0:
            ans.append(temp)
        
        for i in range(len(nums)):
            self.helper(nums[:i] + nums[i + 1:], temp + [nums[i]], ans)
            
            
            
            
#                                temp nums
#                               [] [1, 2, 3]


#            [1][2, 3]                      [2][1, 3]                         [3][1, 2]
#     [1, 2][3]   [1, 3][2]           [2, 1][3]    [2, 3][1]           [3, 1][2]   [3, 2][1]
# [1, 2, 3][]        [1, 3, 2][]   [2, 1, 3][]       [2, 3 ,1][]  [3, 1, 2][]        [3, 2, 1][]

# len(nums) == 0
s=“abcde”
print(s[:2]+s[3:])