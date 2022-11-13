class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arr1 = sorted(arr)
        seen = {}
        self.n = len(arr1)
        self.c = Counter(arr1)
        flow = True
        for key in self.c:
            if self.c[key] in seen:
                flow = False
                break
            else:
                seen[self.c[key]] = 1
        return flow
        
                
    
        



                
    # 제가 생각한 방법은 먼저 문자들을 하나 하나 다 갯수 확인 하여서 갯수를 세고 난 다음에 리스트(tmp)를 만들어 각각의 문자의 갯수를 만든 리스트에다가 넣는다.
    # 그리고 넣은 리스트 요소 요소 갯수를 비교해서 다르면 리턴 false  or True를 한다
        
        
        
        
        
        
        
      