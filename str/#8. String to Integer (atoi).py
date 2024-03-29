ls = list(s.strip())
        
        if len(ls) == 0:
            return 0 
    
        sign = -1 if ls[0] == "-" else 1
        
        if ls[0] in ["+", "-"]:
            del ls[0]
            
        res, i = 0, 0
        while i < len(ls) and ls[i].isdigit():
            res = res* 10 + ord(ls[i]) - ord("0")
            i = i + 1
            
        return max(-2**31, min(sign * res, 2**31 - 1) )
            