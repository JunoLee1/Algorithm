class Solution:
    def divisorGame(self, n: int) -> bool:
        #general : Return true if and only if Alice wins the game, assuming both players play optimally.
        # if n % x == 0 and n == 0, True. n - x = n
        #
                
        if n==1: #n == 1이면 앨리스가 지는 게임
            return False
        for i in range(1,n):
            if n%i==0 and self.divisorGame(n-i)==False: # n 나누기 i 의 나머지가 0 이고 n 다음의 나머지가 0이 아니라면 참 
                return True
        return False# 여기서 잘모르겠어요
    