#題目給定n顆糖果，醫生建議他只能吃最多n/2，要如何在遵循醫生建議的情況下吃下最多不同類型的糖果

class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        return min(len(candyType)//2,len(set(candyType)))
