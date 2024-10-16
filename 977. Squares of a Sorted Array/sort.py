#給定一個list，回傳square後的list
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted( map(lambda x : x**2 ,nums) )
        
