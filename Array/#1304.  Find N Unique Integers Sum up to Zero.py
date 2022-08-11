class Solution:
    def sumZero(self, n: int) -> List[int]:
        a = range(1,n) #the unique tends to mean the different elements. Arranging the array that sum is zero, return not only the range of positive elements are from 1 to i - 1 but also negative elements have same the range of values.
        return list(a) + [-sum(a)] #it is far more important that positive elements' sum is same with negative elements' sum, for the list's sum should be zero.