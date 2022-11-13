class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        #prob def:  Check if All Characters Have Equal Number of Occurrences
        
#         1. tmp 값에다 counter의 val을 다 구한다
#         2. 만약에 tmp값 안에있는 val들이 각각 다른 경우와 같을 경우를 구한다.
        freq = {}
        self.n = len(s)
        flow = True
        for i in range(self.n):
            if s[i] not in freq:
                freq[s[i]] = 1
            else:
                freq[s[i]] += 1
        l = list(freq.values())
        for idx in range(len(l)):
            for j in range(idx):
                if l[idx] != l[j]:
                    flow = False
                    break
                else:
                    flow = True
        return flow
                    





                
    # 제가 생각한 방법은 먼저 문자들을 하나 하나 다 갯수 확인 하여서 갯수를 세고 난 다음에 리스트(tmp)를 만들어 각각의 문자의 갯수를 만든 리스트에다가 넣는다.
    # 그리고 넣은 리스트 요소 요소 갯수를 비교해서 다르면 리턴 false  or True를 한다
        
        
        
        
        
        
        
      