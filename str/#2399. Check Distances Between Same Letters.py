class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        unique = set(s)
        for letter in unique:
            index = s.index(letter)
            dis = distance[ord(letter) - 97]
            if dis + index + 1 > len(s) - 1 or s[dis + index + 1] > letter:
                return False
        return True     