class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        #problem def:return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
       # Create hset for storing previous of k elements...
        seen = {}
        for i in range(len(nums)):
            if nums[i] in seen and abs(i - seen[nums[i]]) <= k :
                return True
            seen.add(nums[i])
            
        return False
    