def removeDuplicate(nums):
    i = 0 
    for j in range(1,len(nums)):
        if nums[j] != nums[i]: #인덱스의 맨첫번째와 두번째가 다른 값을 가질때
            i += 1 #i에다가 1을 더해주고
            nums[i] == nums[j] # 더해준값은 nums[j]값과 같다
    return i + 1
num = [1,1,2]
print(removeDuplicate(num))