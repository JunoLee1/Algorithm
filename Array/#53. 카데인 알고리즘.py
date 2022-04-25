def maxSubArray(nums):
    curr_sum = 0
    for i in range(len(nums)):
        curr_sum += nums[i]
    max_sum = max(curr_sum + nums[i], nums[i])
    return max_sum
num = [5,4,-1,7,8]
print(maxSubArray(num))

        
       
        
        