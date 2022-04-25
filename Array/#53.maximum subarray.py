def maxSubArray(nums):
        curr_sum = 0
        max_sum = nums[0]
        for i in range(len(nums)): 
            curr_sum = max(curr_sum + nums[i], nums[i]) #최댓값을 업데이트를 해준다 
            max_sum = max(curr_sum,max_sum) # curr sum과 이전 max_sum의 최댓값을 다시 max_sum을 업데이트해준다
        return max_sum
num = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(num))

