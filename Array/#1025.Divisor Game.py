class Solution:
    def divisorGame(self, n: int) -> bool:
      # problem def: Return True when Alice wins the game by assuming both players play optimally.
      # Base Case: 
        #if i == 1:
            #return False # if a player cannot a move,  they lose the game. 
        #if i == 2:
            #return True #
        #if i == 3:
            #return False #
      # f(i): given i , return Answer whether Alice is going to win or not 
      # relation: f(i) = i % x == 0 (when 1 % x 's reminder is zero) and the x is between 0 and i-1
        dp = [-1]*(n+1) 
        def topdown(dp, i):     #여기서 n을 쓰면 안되는 이유는         
                                                                    
            if i == 1:           
                return False
            
            if i == 2:
                return True 
            
            if i == 3:
                return False
            
            if dp[i] != -1:
                return dp[i]
            
            for x in range(1, i): 
                if i % x == 0 and not(topdown(dp, i - x)): #승리의 조건
                    dp[i] = True 
                    return dp[i]# (잠깐 저장)dp에 저장하고 rt 해준다
                
            dp[i] = False #이길지 질지 정하는것 이기에 중요하다
            return dp[i] # #
            
        return topdown(dp, n)