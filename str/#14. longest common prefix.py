def longestCommonPrefix(self,strs):
    strs.sort()
    ans = 0
    for i in range(len(strs[0])):
        curr = strs[0][i]
        if self.includeCha(strs,curr,i):
            ans += curr 
        else:
            break
def includeCha(self,strs,curr,i):
    for x in strs[1:]:
        if x[i] == curr:
            continue 
        else:
            return False
    return True

strs1 = ["flower","flow","flight"]
print(longestCommonPrefix(strs1))