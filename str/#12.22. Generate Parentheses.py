class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # generate all combinations of well - formed parenthese
        # if i == 0:
        # return ""
        # if i > j: 
        # f(i) = f(i) + range(f(j))
        
        dp = [[] for _ in range(n + 1)]
        dp[0].append("") # 첫번째 괄호 안엔 다 비어 있다
        for i in range(n + 1):
            for j in range(i):
                dp[i] += ["(" + x + ")" + y for x in dp[j] for y in dp[i - j - 1]]
        return dp[n]
        