class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # problem def : find longest palindromic subsequence's length in s.
        # f(i,j) = longest palindromic subsequence's length in s from i to j.
         #if i == j:
            #return 1
        #if i > j:
            #return 0
        #else :
            #max(f(i-1),f(j-1)) + 2
            n = len(s) #n =5
            
            dp = [[0 for _ in range(n)] for _ in range(n)]
            for i in range(n):
                dp[i][i] = 1
            
            for length in range(2,n+1): #길이를 나열하기 위해서 씀 2
                for i in range(0, n -length + 1):# 왜 n - length  이냐면, length 에따라 i의 인덱스의 움직일수있는 칸이 줄어든다것을 이용한 식이다 
                    j = i + length - 1 # 4 + 2 -1 =5
                    if s[i] == s[j]:
                        dp[i][j] = 2 + dp[i+1][j-1]
                    else:
                        dp[i][j] = max(dp[i+1][j], dp[i][j-1])
            return dp[0][n-1]

              ij
              bbbab 


            
    
    