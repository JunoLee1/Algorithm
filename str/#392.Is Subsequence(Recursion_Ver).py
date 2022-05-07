def isSubsequence(self, s, t):
    if len(s) == 0:
        return True
    if len(s) > len(t):
        return False
    if s[0] == t[0]:
        return self.isSubsequence(s[1:],t[1:])
    else:
        return self.isSubsequence(s,t[1:])

s1 = "abc"
t1 = "ahbgdc"
print(isSubsequence(self,s1,t1))