from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic1 = defaultdict(int)
        dic2 = defaultdict(int)
        for item in s:
            dic1[item] = dic1.get(item,0) + 1
        for item in t:
            dic2[item] = dic2.get(item,0) + 1
        return dic2 == dic1
        