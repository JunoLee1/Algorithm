class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1 
                right += 1
            return s[left + 1 : right]
        
        if  len(s) < 2 or s == s[:: -1]:
            return s
        
        res = ""
        for i in range(len(s)):
            res = max(res, expand(i, i), expand(i, i + 1), key = len)
        return res