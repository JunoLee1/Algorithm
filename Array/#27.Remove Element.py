def removeElement(nums,val):
    count = 0
    for i in range(len(nums)): 
        if nums[i] != val: #nums[i]의 값이 val와 다를때(같을 경우 제거)
            nums[count] = nums[i] #한칸 앞댕긴다
            count += 1
    return count
nums1 = [3,2,2,3]
val1 = 3
print(removeElement(nums1,val1))