class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n+1)
        dp[0] = 1 #to count each 
        if not s:
            return 0
        
        for i in range(1, n + 1):
            
            if s[i - 1] != "0":
                dp[i] += dp[i - 1]
            
            if len(s[i-2 : i]) == 2 and "10" <= s[i-2 : i] <= "26":
                dp[i] += dp[i - 2]
        return dp[n]




    class Solution:
    def numDecodings(self, s: str) -> int:
        #problem def:  return the number of ways to decode from "i - 1" th  to "n" th.
        n  = len(s)
        dp = [-1 for _ in range(len(s))]
        def topdown (i, dp):
            if i == n: #남아 있는 숫자가 없다면 모든 수를 변환 
                return 1
            
            if dp[i] != -1:
                return dp[i]
            
            if s[i] == "0": #남아있는 숫자의 첫째 자리가 "0"이면, 0으로 저장
                dp[i] = 0
            
            if i + 1 < len(s) and int(s[i : i + 2]) < 27: #만약 자리수가 두자리 이상이구 27보다 작다면 
                dp[i] =  topdown(i + 1, dp) + topdown(i + 2, dp)
                #첫번째자리 만 먼저 decoding 하거나 , 두번째자리도 decoding 해서 저장한다
            else:
                dp[i] =  topdown(i + 1, dp) #만약 남아있는 자리가 1자리 뿐이 거나 27보다 크다면  첫번째 자리면 저장한다
            return dp[i] #저장된값을 리턴
        return topdown(0,dp) #인덱스 0부터 대입하여 구해준다.
       
    
        
    


    
    
   
            