class Solution:
    def sortString(self, s: str) -> str:
        d = defaultdict(int)
        res = ""
        for char in s:
            d[char] += 1 #
        
        while True: # True 일동안 
            Flag = True # Flag 함수에다가 boolean True
            for value in d.values():
                if value != 0:
                    Flag = False
                    break
            if Flag:
                break

            for ch in ascii_lowercase: # express increasing lowercase
                if d[ch] > 0: #if there is a ch in dict
                    d[ch] -= 1 # takes a ch from dict to  res
                    res += ch
            for ch in ascii_lowercase[::-1]: #express decreasing lowercase
                if d[ch] > 0: #if there is a ch in dict
                    d[ch] -= 1 # takes a ch from dict to res 
                    res += ch
        return res
            

            

