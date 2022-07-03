class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        freq = Counter(s)
        odd_nums = 0
        
        for num in freq.values():
            if num % 2 == 1:
                odd_nums += 1
        res = len(s) - (odd_nums - 1) if odd_nums != 0 else len(s)
        return res
        