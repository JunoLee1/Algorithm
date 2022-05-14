class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m==1 and n==1:
            return 1
        if (m == 2 and n== 1) or (m == 1 and n ==2):
            return 1
        res=0
        if m>1:
            res+=self.uniquePaths(m-1,n)
        if n>1:
            res+=self.uniquePaths(m,n-1)
        return res


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1

        return self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)
    
    

'''
we could use "back tracking" from the recursive way 
each sum of the "return values" tends to turn out value which is the number of path.

'''