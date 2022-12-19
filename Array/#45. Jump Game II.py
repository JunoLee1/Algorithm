def jump(self, nums: List[int]) -> int:
        n = len(nums) 
        jumps = [0 for k in range(n)] # to memorize how many jumps each person

        jumps[0] = 0
        for i in range(1, n):
            jumps[i] = float("inf")
            for j in range(i):
                if (i <= j + nums[j]) and (jumps[j] != float("inf")):
                    jumps[i] = min(jumps[i], jumps[j] + 1)
                    break
        return jumps[n - 1]

