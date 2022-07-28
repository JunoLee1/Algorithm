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


class Solution:
    def longestCommonPrefix(self, strings, i=0):
        letter = None
        for string in strings: 
            if i >= len(string): #If there is no common prefix, return an empty string ""
                return ""
            if not letter: #letter가 true 이면 
                letter = string[i] #
            elif letter != string[i]: #
                return ""
        return letter + self.longestCommonPrefix(strings, i + 1)