
def climbStairs(self,n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    else :
        return self.climbStairs(n-1)+ self.climbStairs(n-2)
n = 4
print(climbStairs(n))