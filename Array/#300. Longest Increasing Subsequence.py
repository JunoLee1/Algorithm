class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
       # prob def : return the length of the longest strictly increasing subsequence.
       # f(i) = the length of the longest strictly increasing subsequence 
        n = len(nums)
        dp = [1] * n
        
        for i in range(n): #
            for j in range(i): # 뒤의 숫자를 탐색
                if nums[i] > nums[j]: #뒤의 nums가  앞의 nums보다 클때
                    dp[i] = max(dp[j] + 1, dp[i]) #
        return max(dp)



        # 이문제는 만약 i th 인덱스가 i + 1th(j) 인덱스 보다 작으면 (i < j) 이면 길이를 strictly 늘여서 요소들을 구하라.
        # 중요한건 여기에선 i
        # max를 쓰는 이유는 가장 긴 부분 수열을 구하는 것이므로 쓴다 
        # 여기서 for 루프를 쓴 이유는 가장 낮은 인덱스인 0 부터 n-1 까지 무차별적 대입하기 위해서 이구,  2번째 루프로 이전 인덱스와 비교하기위해 사용

        