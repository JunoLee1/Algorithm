class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n+1)
        split = s.split() #랜덤으로 s를 나눠주고
        for i in range(n):
            for as_num in split:
                if len(split[int(as_num)]) <= 3:#숫자의 아스키 넘버를 먼저 구하고, 그숫자들에다가 +64를 더해 준다음 대문자 아스키 넘버를 구하고, 이 아스키 넘버로 대문자들의 갯수를 구해준다 
                    temp[i] += str(int(split[int(as_num)]) + 64)
                    dp[i] = temp[i]
                else:
                    if s[0] == '0':
                        return 0
            return len(dp)