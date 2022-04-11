import numbers


def smallerNumbersThanCurrent(nums):
    mp = {}
    sorted_nums = sorted(nums)
    for i in range(len(nums)):
        if sorted_nums not in mp:
            mp[sorted_nums[i]] = i
    for i in range(len(nums)):
        nums[i] = mp[nums[i]]
    return nums


