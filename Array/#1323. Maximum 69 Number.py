class Solution:
    def maximum69Number (self, num: int) -> int:
        num = str(num) # to modify integer convert from integer to string  
        uniq = {} # to save "6" and "9" 
        for i in range(len(num)):
            if num[i] == "6": 
                uniq[i] = "9"
            else:
                uniq[i] = "6"
        for idx in uniq: 
            if uniq[idx] == "9": # if there is "6" in num, changes the part to 9 one most digit
                return int(num[:idx] + uniq[idx] + num[idx+1:]) # changes one most number 

        return int(num) #왜 한칸더 인덴테이션 더해야하나요??
        